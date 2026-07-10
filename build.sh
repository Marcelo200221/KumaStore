#!/usr/bin/env bash
# Salir inmediatamente si un comando falla
set -o errexit

# 1. Instalar dependencias
pip install -r requirements.txt

# 2. Recopilar archivos estáticos
python manage.py collectstatic --no-input

# 3. Crear los archivos de migración en el servidor (por si acaso)
python manage.py makemigrations --no-input

# 4. Aplicar las migraciones a Supabase (creará las tablas que faltan)
python manage.py migrate --no-input

# 5. Cargar los productos y categorías
python manage.py preload