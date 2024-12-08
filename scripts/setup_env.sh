#!/bin/bash

# Script to set up the environment for Stegsolve Clone

echo "Setting up virtual environment..."
python3 -m venv venv

echo "Activating virtual environment..."
source venv/bin/activate

echo "Installing dependencies..."
pip install -r requirements.txt

echo "Setup complete! Activate your environment with 'source venv/bin/activate'."