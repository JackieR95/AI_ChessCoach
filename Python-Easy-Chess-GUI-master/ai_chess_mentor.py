"""
# Written by Jacqueline Rael and Copilot Agent
# Date: 12/09/2025
# Lab: Final Project

ai_chess_mentor.py

A Chess Mentor module that:
- Evaluates moves using Stockfish
- Gets AI explanations using Google Gemini
- Provides move quality feedback to the GUI
"""

import chess
import chess.engine
import os
import logging
from pathlib import Path
from dotenv import load_dotenv

# Try to import Google Generative AI
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False
    logging.warning("google-generativeai not installed. AI explanations will be disabled.")

# Load environment variables
load_dotenv()

# Configure logging
logger = logging.getLogger(__name__)


class ChessMentor:
    """AI Chess Mentor for move evaluation and explanation"""

    def __init__(self, stockfish_path=None, use_gemini=True):
        """
        Initialize Chess Mentor

        Args:
            stockfish_path: Path to Stockfish engine. If None, tries to find it.
            use_gemini: Whether to use Google Gemini for explanations
        """
        self.engine = None
        self.stockfish_path = stockfish_path or self._find_stockfish()
        self.use_gemini = use_gemini and GEMINI_AVAILABLE
        self.gemini_model = None

        # Initialize Stockfish engine
        if self.stockfish_path and os.path.exists(self.stockfish_path):
            try:
                self.engine = chess.engine.SimpleEngine.popen_uci(self.stockfish_path)
                logger.info(f"Stockfish engine loaded: {self.stockfish_path}")
            except Exception as e:
                logger.error(f"Failed to load Stockfish: {e}")
                self.engine = None
        else:
            logger.warning("Stockfish engine not found. Move evaluation disabled.")

        # Initialize Gemini
        if self.use_gemini:
            try:
                api_key = os.getenv('GOOGLE_GEMINI_API_KEY')
                if not api_key:
                    logger.warning("GOOGLE_GEMINI_API_KEY not found in .env")
                    self.use_gemini = False
                else:
                    genai.configure(api_key=api_key)

                    # Try a small list of likely-available models (based on list_models)
                    candidate_models = [
                        'models/gemini-2.5-flash',
                        'models/gemini-2.5-pro',
                        'models/gemini-flash-latest',
                        'models/gemini-2.0-flash',
                        'models/gemini-pro-latest',
                    ]

                    self.gemini_model = None
                    for model_name in candidate_models:
                        try:
                            test_model = genai.GenerativeModel(model_name)
                            # Probe once to confirm availability
                            test_model.generate_content("ok")
                            self.gemini_model = test_model
                            logger.info(f"Google Gemini initialized with model: {model_name}")
                            break
                        except Exception as model_err:
                            logger.warning(f"Gemini model {model_name} failed: {model_err}")

                    if not self.gemini_model:
                        logger.error("No Gemini model could be initialized from candidate list")
                        self.use_gemini = False
            except Exception as e:
                logger.error(f"Failed to initialize Gemini: {e}")
                self.use_gemini = False

    def _find_stockfish(self):
        """Try to find Stockfish in common locations"""
        common_paths = [
            'Engines/stockfish-windows-x86-64-avx2.exe',  # Windows AVX2 version
            'Engines/stockfish-windows-x86-64.exe',       # Windows generic
            'Engines/stockfish',
            'Engines/stockfish.exe',
            'stockfish',
            'stockfish.exe',
        ]

        for path in common_paths:
            if os.path.exists(path):
                logger.info(f"Found Stockfish at: {path}")
                return path

        logger.warning("Stockfish not found in common locations")
        return None

    def evaluate_move(self, board, move, depth=20, time_limit=1):
        """
        Evaluate a move using Stockfish

        Args:
            board: chess.Board object
            move: chess.Move object
            depth: Search depth (default 20)
            time_limit: Time limit in seconds (default 1)

        Returns:
            dict with keys: 'score', 'mate', 'quality', 'explanation'
        """
        if not self.engine:
            logger.warning("Stockfish engine not available for evaluation - returning basic assessment")
            # Fallback: return Neutral quality for all moves
            return {
                'score': None,
                'mate': None,
                'quality': '= Neutral (engine unavailable)',
                'score_diff': 0,
                'explanation': 'Engine analysis not available'
            }

        try:
            # Get evaluation before the move
            info_before = self.engine.analyse(
                board,
                chess.engine.Limit(depth=depth, time=time_limit)
            )
            score_before = info_before.get('score')
            logger.debug(f"Score before move: {score_before}")

            # Make the move and evaluate
            board_copy = board.copy()
            board_copy.push(move)

            info_after = self.engine.analyse(
                board_copy,
                chess.engine.Limit(depth=depth, time=time_limit)
            )
            score_after = info_after.get('score')
            logger.debug(f"Score after move: {score_after}")

            # Calculate move quality
            quality, score_diff = self._calculate_quality(
                score_before, score_after, board.turn
            )
            logger.debug(f"Move quality calculated: {quality}, diff: {score_diff}")

            return {
                'score': score_after,
                'mate': info_after.get('mate'),
                'quality': quality,
                'score_diff': score_diff,
                'explanation': None  # Will be filled by Gemini
            }

        except Exception as e:
            logger.error(f"Error evaluating move: {e}", exc_info=True)
            return {
                'score': None,
                'mate': None,
                'quality': 'Error',
                'explanation': f"Evaluation error: {str(e)}"
            }

    def _score_to_cp(self, score_obj, pov_color):
        """Convert a chess.engine.PovScore/Score to centipawns from pov_color."""
        if score_obj is None:
            return 0  # Return 0 instead of None for neutral position

        try:
            # PovScore: use .pov(color).score() for a signed cp value
            if isinstance(score_obj, chess.engine.PovScore):
                cp_value = score_obj.pov(pov_color).score(mate_score=100000)
                return cp_value if cp_value is not None else 0

            # Score: convert to PovScore via .pov()
            if isinstance(score_obj, chess.engine.Score):
                cp_value = score_obj.pov(pov_color).score(mate_score=100000)
                return cp_value if cp_value is not None else 0

            # Fallback: already numeric
            return float(score_obj) if score_obj else 0
        except Exception as e:
            logger.warning(f"Error converting score to centipawns: {e}")
            return 0

    def _calculate_quality(self, score_before, score_after, is_white):
        """
        Calculate move quality based on score change

        Returns:
            tuple: (quality_string, score_difference)
        """
        # If either score is None, we can't calculate quality
        if score_before is None and score_after is None:
            return 'Unknown', None

        before_cp = self._score_to_cp(score_before, chess.WHITE if is_white else chess.BLACK)
        after_cp = self._score_to_cp(score_after, chess.WHITE if is_white else chess.BLACK)

        score_diff = after_cp - before_cp

        # Determine quality
        if score_diff >= 50:
            quality = '⭐ Excellent'
        elif score_diff >= 15:
            quality = '✓ Good'
        elif score_diff >= -15:
            quality = '= Neutral'
        elif score_diff >= -50:
            quality = '⚠️ Questionable'
        else:
            quality = '❌ Blunder'

        return quality, score_diff

    def get_move_explanation(self, board, move, quality_info):
        """
        Get AI explanation of the move using Gemini

        Args:
            board: chess.Board object before the move
            move: chess.Move object
            quality_info: dict from evaluate_move()

        Returns:
            str: AI explanation of the move
        """
        if not self.use_gemini or not self.gemini_model:
            return None

        try:
            # Get move notation
            san_move = board.san(move)

            # Build prompt
            prompt = f"""You are a chess mentor. Briefly explain the move '{san_move}' in chess position:

FEN: {board.fen()}

The move quality is: {quality_info.get('quality', 'Unknown')}

Provide a 1-2 sentence explanation of why this move is {quality_info.get('quality', 'Unknown')}.
Focus on chess principles (control, development, tactics, etc).
Keep it concise and educational."""

            # Call Gemini
            response = self.gemini_model.generate_content(prompt)
            explanation = response.text.strip()

            logger.info(f"Gemini explanation received for move {san_move}")
            return explanation

        except Exception as e:
            logger.error(f"Error getting Gemini explanation: {e}")
            return None

    def analyze_move(self, board, move, depth=20, time_limit=1):
        """
        Complete move analysis: evaluate + explain

        Args:
            board: chess.Board object
            move: chess.Move object
            depth: Stockfish depth
            time_limit: Stockfish time limit

        Returns:
            dict with complete analysis
        """
        # Evaluate with Stockfish
        evaluation = self.evaluate_move(board, move, depth, time_limit)

        # Get explanation from Gemini
        if evaluation['quality'] != 'Error':
            explanation = self.get_move_explanation(board, move, evaluation)
            evaluation['explanation'] = explanation

        return evaluation

    def format_output(self, san_move, analysis):
        """
        Format analysis for GUI display

        Args:
            san_move: Move in algebraic notation
            analysis: dict from analyze_move()

        Returns:
            str: Formatted output for comment box
        """
        output = f"Move: {san_move}\n"
        
        # Get quality with debugging
        quality = analysis.get('quality', 'Unknown')
        logger.debug(f"Format output - Quality: {quality}")
        output += f"Quality: {quality}\n"

        if analysis.get('score_diff') is not None:
            try:
                output += f"Score Change: {analysis['score_diff']:+.1f}cp\n"
            except (ValueError, TypeError):
                output += f"Score Change: {analysis['score_diff']}cp\n"

        if analysis.get('explanation'):
            output += f"\n{analysis['explanation']}\n"
        else:
            # Show if no explanation was available
            if not quality.startswith('⭐') and not quality.startswith('✓') and not quality.startswith('=') and not quality.startswith('⚠️') and not quality.startswith('❌'):
                output += "\n(Stockfish analysis not available)\n"

        return output

    def close(self):
        """Close the Stockfish engine"""
        if self.engine:
            try:
                self.engine.quit()
                logger.info("Stockfish engine closed")
            except Exception as e:
                logger.error(f"Error closing engine: {e}")


# Example usage
if __name__ == "__main__":
    # Test the mentor
    mentor = ChessMentor()

    # Create a test position
    board = chess.Board()
    move = board.parse_san("e4")

    # Analyze the move
    analysis = mentor.analyze_move(board, move)
    output = mentor.format_output("e4", analysis)
    print(output)

    mentor.close()
