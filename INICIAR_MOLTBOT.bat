@echo off
cls
title Bot Antigravity Launcher
color 0A
echo ============================================
echo   STARTING AUTO-MANAGEMENT SYSTEM
echo ============================================
echo.

:: --- CONFIGURATION ---
set "PROYECTO=%~dp0"
set "PROYECTO=%PROYECTO:~0,-1%"

echo [1/4] Verifying project folder...
if not exist "%PROYECTO%" (
    color 0C
    echo [!] ERROR: Project folder does not exist.
    echo Path searched: %PROYECTO%
    pause
    exit
)
echo     OK: Folder found.

cd /d "%PROYECTO%"

echo [2/4] Verifying virtual environment...
if not exist ".venv\Scripts\python.exe" (
    echo     [!] Environment not found. Creating a new one...
    py -m venv .venv >nul 2>&1
    if errorlevel 1 (
        python -m venv .venv >nul 2>&1
    )
    
    if not exist ".venv\Scripts\python.exe" (
        color 0C
        echo [!] ERROR: Could not create virtual environment. 
        echo     Ensure Python is installed and added to PATH.
        pause
        exit
    )
    
    echo     [OK] Environment created. Installing dependencies...
    echo     (Please wait, this may take a minute)
    echo.
    ".venv\Scripts\python.exe" -m pip install -r requirements.txt
    echo.
    echo     [OK] Dependencies installed.
) else (
    echo     OK: Environment found.
)

echo [3/4] Verifying main script...
if not exist "Boton_Run.py" (
    color 0C
    echo [!] ERROR: File 'Boton_Run.py' is missing.
    pause
    exit
)
echo     OK: Script found.

echo [4/4] EXECUTING BOT...
echo --------------------------------------------
".venv\Scripts\python.exe" "Boton_Run.py"
echo --------------------------------------------

echo.
echo [INFO] Program has finished.
if %errorlevel% neq 0 (
    color 0C
    echo [!] An ERROR occurred with code: %errorlevel%
) else (
    echo [OK] Finished successfully.
)

pause
