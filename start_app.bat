@echo off
chcp 65001 > nul
echo ========================================================
echo   Starting PMSAMPSIZE App (Light Mode)
echo ========================================================

cd /d "%~dp0"

:: 1. Check Python
python --version > nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed or not in PATH.
    echo Please install Python from https://www.python.org/downloads/
    pause
    exit /b
)

:: 2. Install Dependencies (Directly to System/User, skipping heavy venv)
echo [INFO] Checking/Installing libraries...
pip install -q --no-warn-script-location -r pmsampsize_app\requirements.txt

:: 3. Run App
echo.
echo [INFO] Launching Application...
echo    Browser will open automatically.
echo.

streamlit run pmsampsize_app\app.py

if errorlevel 1 (
    echo.
    echo [ERROR] Application crashed.
    pause
)
