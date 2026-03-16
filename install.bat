@echo off
REM AttackAIO Crypto - Installation Script for Windows
REM ⚠️ WARNING: Only use this tool to recover YOUR OWN lost passphrases

echo ========================================
echo   AttackAIO Crypto - Installer
echo   ^! LEGITIMATE USE ONLY ^!
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo X Error: Python is not installed or not in PATH.
    echo Please install Python 3.8 or higher from https://python.org
    pause
    exit /b 1
)

echo [OK] Python found: 
python --version
echo.

REM Check if pip is installed
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo X Error: pip is not installed or not in PATH.
    echo Please install pip for Python.
    pause
    exit /b 1
)

echo [OK] pip found
echo.

REM Upgrade pip
echo [*] Upgrading pip...
python -m pip install --upgrade pip --quiet

REM Install dependencies
echo [*] Installing dependencies...
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo.
    echo ========================================
    echo   INSTALLATION COMPLETED SUCCESSFULLY!
    echo ========================================
    echo.
    echo   IMPORTANT REMINDERS:
    echo ========================================
    echo ^!  This tool is for EDUCATIONAL purposes
    echo ^!  Only use on wallets YOU OWN
    echo ^!  Unauthorized access is ILLEGAL
    echo ========================================
    echo.
    echo To run a specific coin script:
    echo   python bitcoin.py
    echo   python ethereum.py
    echo   python doge.py
    echo.
    echo You will need a word list file ^<words.txt^)
    echo Example: copy words.txt.example words.txt
    echo.
) else (
    echo.
    echo X Installation failed. Please check the errors above.
)

pause
