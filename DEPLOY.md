# 🚀 Deploy no Railway - Guia Completo

## 📋 Pré-requisitos

- Conta no [Railway](https://railway.app/)
- Git instalado
- Projeto Django configurado

## 🔧 Configuração no Railway

### 1️⃣ Criar Novo Projeto no Railway

1. Acesse [railway.app](https://railway.app/)
2. Clique em **"New Project"**
3. Escolha **"Deploy from GitHub repo"** (ou "Empty Project")

### 2️⃣ Adicionar PostgreSQL

1. No seu projeto, clique em **"+ New"**
2. Selecione **"Database"** → **"Add PostgreSQL"**
3. O Railway criará automaticamente o banco de dados

### 3️⃣ Configurar Variáveis de Ambiente

No painel do Railway, vá em **"Variables"** e adicione:

```bash
# URL do Banco de Dados (copie do PostgreSQL criado)
DATABASE_URL=postgresql://postgres:VocWqTPORrjLlfMkAIKNZfsHUIKQYXfJ@postgres.railway.internal:5432/railway

# Secret Key (gere uma nova chave segura)
SECRET_KEY=sua-chave-super-secreta-aqui-minimum-50-caracteres

# Debug Mode (SEMPRE False em produção)
DEBUG=False

# Hosts Permitidos (domínio do Railway)
ALLOWED_HOSTS=*.railway.app

# Porta (opcional, Railway define automaticamente)
PORT=8000
```

### 4️⃣ Como Pegar a DATABASE_URL

No Railway:
1. Clique no serviço **PostgreSQL**
2. Vá na aba **"Connect"**
3. Copie a **"Postgres Connection URL"** 
4. **IMPORTANTE**: Se a URL tiver `postgres.railway.internal`, ela só funciona internamente no Railway
5. Para conexão externa, use a URL pública com o host externo

**Formato da URL:**
```
postgresql://usuario:senha@host:porta/database
```

### 5️⃣ Gerar SECRET_KEY Segura

Execute no Python:
```python
import secrets
print(secrets.token_urlsafe(50))
```

Ou use este comando no terminal:
```bash
python -c "import secrets; print(secrets.token_urlsafe(50))"
```

## 📦 Deploy

### Opção 1: Deploy via GitHub (Recomendado)

1. **Inicialize o Git** (se ainda não fez):
```bash
git init
git add .
git commit -m "Configuração inicial para deploy"
```

2. **Crie um repositório no GitHub** e faça push:
```bash
git remote add origin https://github.com/seu-usuario/seu-repo.git
git branch -M main
git push -u origin main
```

3. **No Railway**:
   - Clique em **"+ New"** → **"GitHub Repo"**
   - Selecione seu repositório
   - O Railway fará o deploy automaticamente

### Opção 2: Deploy via Railway CLI

1. **Instale o Railway CLI**:
```bash
npm i -g @railway/cli
```

2. **Login no Railway**:
```bash
railway login
```

3. **Link com o projeto**:
```bash
railway link
```

4. **Deploy**:
```bash
railway up
```

## 🗄️ Executar Migrações

Depois do deploy, execute as migrações:

### Via Railway Dashboard:
1. Vá em **"Settings"** → **"Deploy"**
2. Em **"Custom Start Command"**, temporariamente adicione:
```bash
python manage.py migrate && gunicorn agenda.wsgi
```

### Via Railway CLI:
```bash
railway run python manage.py migrate
```

### Criar Superusuário:
```bash
railway run python manage.py createsuperuser
```

### Criar Contatos de Exemplo:
```bash
railway run python manage.py criar_contatos_exemplo
```

## 🔍 Comandos Úteis

### Ver Logs:
```bash
railway logs
```

### Executar Comando no Railway:
```bash
railway run [seu-comando]
```

### Coletar Arquivos Estáticos:
```bash
railway run python manage.py collectstatic --noinput
```

## ✅ Checklist de Deploy

- [ ] PostgreSQL adicionado no Railway
- [ ] Variáveis de ambiente configuradas
  - [ ] DATABASE_URL
  - [ ] SECRET_KEY (nova e segura)
  - [ ] DEBUG=False
  - [ ] ALLOWED_HOSTS
- [ ] Código enviado para GitHub/Railway
- [ ] Deploy realizado com sucesso
- [ ] Migrações executadas
- [ ] Superusuário criado
- [ ] Arquivos estáticos coletados
- [ ] Site acessível no domínio do Railway

## 🌐 Acessar sua Aplicação

Após o deploy, o Railway fornecerá uma URL como:
```
https://seu-app.up.railway.app
```

## 🔒 Segurança

### ⚠️ IMPORTANTE:

1. **Nunca** commite `.env` ou arquivos com senhas
2. **Sempre** use `DEBUG=False` em produção
3. **Gere** uma nova `SECRET_KEY` (não use a padrão)
4. **Configure** `ALLOWED_HOSTS` corretamente
5. **Use** HTTPS (Railway fornece automaticamente)

## 🐛 Troubleshooting

### Erro 500:
- Verifique os logs: `railway logs`
- Confira se `DEBUG=False` e `ALLOWED_HOSTS` está correto
- Execute as migrações

### Banco de dados não conecta:
- Verifique se a `DATABASE_URL` está correta
- Certifique-se que o PostgreSQL está rodando
- Use a URL interna (`postgres.railway.internal`) para serviços no Railway

### Arquivos estáticos não carregam:
- Execute: `railway run python manage.py collectstatic --noinput`
- Verifique se o WhiteNoise está instalado
- Confira `STATIC_ROOT` e `STATICFILES_STORAGE` no settings.py

### Migrações não aplicadas:
```bash
railway run python manage.py migrate
```

## 📚 Recursos Adicionais

- [Documentação Railway](https://docs.railway.app/)
- [Django Deployment Checklist](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/)
- [Railway Templates](https://railway.app/templates)

## 💡 Dicas

1. Use o **Railway CLI** para facilitar o desenvolvimento
2. Configure **GitHub Actions** para CI/CD automático
3. Monitore os **logs** regularmente
4. Configure **backups** do banco de dados
5. Use **variáveis de ambiente** para todas as configurações sensíveis

---

**Seu projeto está pronto para produção!** 🎉
