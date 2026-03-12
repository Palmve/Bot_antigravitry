@echo off
cls
title Lanzador de Bot Antigravity
color 0A
echo ============================================
echo   INICIANDO SISTEMA DE AUTO-GESTION
echo ============================================
echo.

:: --- CONFIGURACION ---
set "PROYECTO=%~dp0"
set "PROYECTO=%PROYECTO:~0,-1%"

echo [1/4] Verificando carpeta del proyecto...
if not exist "%PROYECTO%" (
    color 0C
    echo [!] ERROR: La carpeta del proyecto no existe.
    echo Ruta buscada: %PROYECTO%
    pause
    exit
)
echo     OK: Carpeta encontrada.

cd /d "%PROYECTO%"

echo [2/4] Verificando entorno virtual...
if not exist ".venv\Scripts\python.exe" (
    echo     [!] Entorno no encontrado. Creando uno nuevo...
    py -m venv .venv >nul 2>&1
    if errorlevel 1 (
        python -m venv .venv >nul 2>&1
    )
    
    if not exist ".venv\Scripts\python.exe" (
        color 0C
        echo [!] ERROR: No se pudo crear el entorno virtual. 
        echo     Asegurate de tener Python instalado y en el PATH.
        pause
        exit
    )
    
    echo     [OK] Entorno creado. Instalando dependencias...
    ".venv\Scripts\python.exe" -m pip install -r requirements.txt >nul
    echo     [OK] Dependencias instaladas.
) else (
    echo     OK: Entorno encontrado.
)

echo [3/4] Verificando script principal...
if not exist "Boton_Run.py" (
    color 0C
    echo [!] ERROR: Falta el archivo 'Boton_Run.py'.
    pause
    exit
)
echo     OK: Script encontrado.

echo [4/4] EJECUTANDO BOT...
echo --------------------------------------------
".venv\Scripts\python.exe" "Boton_Run.py"
echo --------------------------------------------

echo.
echo [INFO] El programa ha terminado.
if %errorlevel% neq 0 (
    color 0C
    echo [!] Ocurrio un ERROR con codigo: %errorlevel%
) else (
    echo [OK] Finalizado correctamente.
)

pause
