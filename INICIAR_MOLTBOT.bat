@echo off
cls
title Lanceur Bot Antigravity
color 0A
echo ============================================
echo   DEMARRAGE DU SYSTEME D'AUTO-GESTION
echo ============================================
echo.

:: --- CONFIGURATION ---
set "PROYECTO=%~dp0"
set "PROYECTO=%PROYECTO:~0,-1%"

echo [1/4] Verification du dossier du projet...
if not exist "%PROYECTO%" (
    color 0C
    echo [!] ERREUR: Le dossier du projet n'existe pas.
    echo Chemin recherche: %PROYECTO%
    pause
    exit
)
echo     OK: Dossier trouve.

cd /d "%PROYECTO%"

echo [2/4] Verification de l'environnement virtuel...
if not exist ".venv\Scripts\python.exe" (
    echo     [!] Environnement non trouve. Creation en cours...
    py -m venv .venv >nul 2>&1
    if errorlevel 1 (
        python -m venv .venv >nul 2>&1
    )
    
    if not exist ".venv\Scripts\python.exe" (
        color 0C
        echo [!] ERREUR: Impossible de creer l'environnement virtuel. 
        echo     Assurez-vous que Python est installe et dans le PATH.
        pause
        exit
    )
    
    echo     [OK] Environnement cree. Installation des dependances...
    echo     (Veuillez patienter, cela peut prendre une minute)
    echo.
    ".venv\Scripts\python.exe" -m pip install -r requirements.txt
    echo.
    echo     [OK] Dependances installees.
) else (
    echo     OK: Environnement trouve.
)

echo [3/4] Verification du script principal...
if not exist "Boton_Run.py" (
    color 0C
    echo [!] ERREUR: Le fichier 'Boton_Run.py' est manquant.
    pause
    exit
)
echo     OK: Script trouve.

echo [4/4] EXECUTION DU BOT...
echo --------------------------------------------
".venv\Scripts\python.exe" "Boton_Run.py"
echo --------------------------------------------

echo.
echo [INFO] Le programme est termine.
if %errorlevel% neq 0 (
    color 0C
    echo [!] Une ERREUR est survenue avec le code: %errorlevel%
) else (
    echo [OK] Termine avec succes.
)

pause
