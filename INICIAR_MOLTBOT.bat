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

echo [2/4] Verificando Python en entorno virtual...
if not exist ".venv\Scripts\python.exe" (
    color 0C
    echo [!] ERROR: No se encuentra '.venv\Scripts\python.exe'.
    echo     Asegurate de haber instalado las dependencias.
    pause
    exit
)
echo     OK: Python encontrado.

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
