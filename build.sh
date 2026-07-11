#!/usr/bin/env bash
# Salir inmediatamente si un comando falla
set -o errexit

# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Recopilar archivos estáticos
echo "=== RECOPILANDO ARCHIVOS ESTATICOS ==="
if !python manage.py collectstatic --no-input; then
    echo "ERROR CRITICO: El comando 'collectstatic' fallo. Rstreo del error:"
    python manage.py collectstatic --no-input 2>&1
    exit 1
fi

# 3. Crear los archivos de migración en el servidor (por si acaso)
echo "=== INICIANDO MIGRACIONES EN PRODUCCIÓN ==="
if ! python manage.py makemigrations --no-input; then
    echo "❌ ERROR CRÍTICO: El comando 'makemigrations' falló. Rastreo del error:"
    python manage.py makemigrations --no-input 2>&1
    exit 1
fi

# 4. Aplicar las migraciones a Supabase (creará las tablas que faltan)
echo "=== INICIANDO MIGRACIONES EN PRODUCCIÓN ==="
if ! python manage.py migrate --no-input; then
    echo "❌ ERROR CRÍTICO: El comando 'migrate' falló. Rastreo del error:"
    python manage.py migrate --no-input 2>&1
    exit 1
fi
# 5. Cargar los productos y categorías
echo "=== INICIANDO SCRIPT PRELOAD ==="
if ! python manage.py preload; then
    echo "❌ ERROR CRÍTICO: El comando 'preload' falló. Rastreo del error:"
    python manage.py preload 2>&1
    exit 1
fi
echo "=== PROCESO DE CONSTRUCCIÓN FINALIZADO CON ÉXITO ==="