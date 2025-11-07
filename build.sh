#!/bin/bash

# Exit on error
set -e

echo "🔧 Instalando dependências..."
pip install --upgrade pip
pip install -r requirements.txt

echo "� Criando diretório staticfiles..."
mkdir -p staticfiles

echo "�📦 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput --clear

echo "🗄️ Executando migrações..."
python manage.py migrate --noinput

echo "✅ Build concluído com sucesso!"
