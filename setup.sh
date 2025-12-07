#!/bin/bash
# Python Easy Chess GUI - Quick Start Script for macOS/Linux

echo ""
echo "========================================"
echo "Python Easy Chess GUI - Setup Script"
echo "========================================"
echo ""

# Check if Python 3.12+ is installed
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python 3 is not installed!"
    echo "Please install Python 3.12 or later from https://www.python.org/downloads/"
    exit 1
fi

echo "Checking Python version..."
python3 --version

# Create virtual environment
if [ ! -d "venv" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv venv
    if [ $? -ne 0 ]; then
        echo "ERROR: Failed to create virtual environment!"
        exit 1
    fi
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate

# Install/upgrade pip
echo ""
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Install requirements
echo ""
echo "Installing dependencies..."
pip install -r SETUP_REQUIREMENTS.txt
if [ $? -ne 0 ]; then
    echo "ERROR: Failed to install dependencies!"
    exit 1
fi

echo ""
echo "========================================"
echo "Setup completed successfully!"
echo "========================================"
echo ""
echo "To run the Chess GUI, execute:"
echo "  cd Python-Easy-Chess-GUI-master"
echo "  python python_easy_chess_gui.py"
echo ""
