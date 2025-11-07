#!/bin/bash

# Script para auxiliar no deploy do Django no Railway

echo "🚀 Preparando aplicação para deploy no Railway..."

# Coletar arquivos estáticos
echo "📦 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

# Executar migrações
echo "🗄️ Executando migrações..."
python manage.py migrate --noinput

# Criar superusuário (opcional)
echo "👤 Para criar superusuário, execute:"
echo "railway run python manage.py createsuperuser"

echo "✅ Deploy preparado com sucesso!"
echo "🌐 Agora faça o push para o Railway ou GitHub"
