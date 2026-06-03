@echo off
echo ====================================
echo   Sistema Taller Automotriz
echo ====================================
echo.

:: Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado.
    echo Descargalo de https://www.python.org
    pause
    exit /b
)

:: Instalar dependencias si no estan
echo Instalando dependencias...
pip install flask openpyxl --quiet

echo.
echo Iniciando servidor...
echo Abri tu navegador en:  http://localhost:5000
echo Para cerrar: presiona Ctrl+C
echo.
python app.py
pause
