@echo off
title Binance Crypto Box Bot - Auto Setup Pro
setlocal EnableDelayedExpansion

cd /d "%~dp0"
echo [1/6] Buscando carpeta con main.py...

:: Buscar la carpeta que contiene main.py
set "botdir="
for /R %%F in (main.py) do (
    set "botdir=%%~dpF"
    goto found
)

:found
if not defined botdir (
    echo ❌ ERROR: No se encontró main.py en ninguna subcarpeta.
    pause
    exit /b
)

echo ✅ Se encontró main.py en: !botdir!
cd /d "!botdir!"

:: Verificar y mover headers.json si está en lugar incorrecto
if not exist "headers.json" (
    echo [2/6] Buscando headers.json...
    for /R %%H in (headers.json) do (
        if /I not "%%~dpH"=="!botdir!" (
            echo ✅ Moviendo headers.json desde: %%~dpH
            move /Y "%%~fH" "headers.json" >nul
        )
    )
)

:: Confirmar que ahora sí exista
if not exist "headers.json" (
    echo ❌ ERROR: No se encontró headers.json. Por favor colócalo junto a main.py
    pause
    exit /b
)

:: Instalar dependencias
echo [3/6] Instalando dependencias...
pip install -r requirements.txt

:: Ejecutar el bot
echo [4/6] Iniciando bot...
python main.py

echo [✔] Todo se ejecutó correctamente.
pause
