#!/bin/bash

# Build script para Railway

echo "🔧 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

echo "📦 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear

echo "✅ Build concluído com sucesso!"
