#!/bin/bash
echo "===================================="
echo "  Sistema Taller Automotriz"
echo "===================================="
echo ""
echo "Instalando dependencias..."
pip3 install flask openpyxl --quiet
echo ""
echo "Iniciando servidor..."
echo "Abri tu navegador en:  http://localhost:5000"
echo "Para cerrar: presiona Ctrl+C"
echo ""
python3 app.py
