#!/bin/bash

# AttackAIO Crypto - Installation Script for Linux/Mac
# ⚠️ WARNING: Only use this tool to recover YOUR OWN lost passphrases

echo "========================================"
echo "  AttackAIO Crypto - Installer"
echo "  ⚠️ LEGITIMATE USE ONLY ⚠️"
echo "========================================"
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Error: Python 3 is not installed."
    echo "Please install Python 3.8 or higher first."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Check if pip is installed
if ! command -v pip3 &> /dev/null; then
    echo "❌ Error: pip3 is not installed."
    echo "Please install pip for Python 3 first."
    exit 1
fi

echo "✓ pip3 found: $(pip3 --version)"
echo ""

# Upgrade pip
echo "📦 Upgrading pip..."
python3 -m pip install --upgrade pip --quiet

# Install dependencies
echo "📦 Installing dependencies..."
python3 -m pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Installation completed successfully!"
    echo ""
    echo "========================================"
    echo "  IMPORTANT REMINDERS:"
    echo "========================================"
    echo "⚠️  This tool is for EDUCATIONAL purposes"
    echo "⚠️  Only use on wallets YOU OWN"
    echo "⚠️  Unauthorized access is ILLEGAL"
    echo "========================================"
    echo ""
    echo "To run a specific coin script:"
    echo "  python3 bitcoin.py"
    echo "  python3 ethereum.py"
    echo "  python3 doge.py"
    echo ""
    echo "You will need a word list file (words.txt)"
    echo "Example: cp words.txt.example words.txt"
    echo ""
else
    echo ""
    echo "❌ Installation failed. Please check the errors above."
    exit 1
fi
