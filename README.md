# 📇 Agenda Eletrônica

Dupla: Eric Assis e Raimundo
Link da aplicação: https://web-production-f7ba5.up.railway.app/

Uma aplicação web moderna e intuitiva para gerenciar seus contatos pessoais e profissionais, desenvolvida com Django e Tailwind CSS.

## ✨ Características

### 🎨 Design Moderno
- Interface limpa e responsiva com Tailwind CSS
- Animações suaves e transições elegantes
- Ícones do Font Awesome
- Gradientes e efeitos visuais modernos

### 📋 Funcionalidades Principais

#### Gestão de Contatos
- ✅ **Criar** novos contatos com múltiplos campos
- 👁️ **Visualizar** detalhes completos de cada contato
- ✏️ **Editar** informações existentes
- 🗑️ **Excluir** contatos com confirmação de segurança
- ⭐ **Favoritar** contatos importantes

#### Informações do Contato
- Nome completo (obrigatório)
- E-mail
- Telefone e Celular
- Endereço completo
- Categoria (Família, Amigo, Trabalho, Outros)
- Empresa e Cargo
- Data de aniversário
- Observações personalizadas

#### Recursos
- 🔍 **Busca avançada** por nome, email, telefone ou empresa
- 🏷️ **Filtros** por categoria
- ⭐ **Filtro de favoritos**
- 📄 **Paginação** (12 contatos por página)
- 📊 **Dashboard** com estatísticas
- 🎨 **Avatares coloridos** com iniciais

## 🚀 Como Usar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação e Desenvolvimento Local

1. **Clone o repositório ou navegue até a pasta do projeto:**
```bash
cd C:\Users\Eric\Desktop\faculdade\python-app
```

2. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

3. **Execute as migrações:**
```bash
python manage.py migrate
```

4. **Crie contatos de exemplo (opcional):**
```bash
python manage.py criar_contatos_exemplo
```

5. **Inicie o servidor de desenvolvimento:**
```bash
python manage.py runserver
```

6. **Acesse no navegador:**
```
http://127.0.0.1:8000/
```


## 📁 Estrutura do Projeto

```
python-app/
├── agenda/                 # Configurações do projeto
│   ├── settings.py        # Configurações gerais
│   ├── urls.py           # URLs principais
│   └── wsgi.py
├── contatos/              # App de contatos
│   ├── models.py         # Modelo Contato
│   ├── views.py          # Views (lógica)
│   ├── forms.py          # Formulários
│   ├── urls.py           # URLs do app
│   └── admin.py          # Configuração do admin
├── templates/             # Templates HTML
│   ├── base.html         # Template base
│   └── contatos/         # Templates do app
│       ├── lista_contatos.html
│       ├── detalhes_contato.html
│       ├── form_contato.html
│       └── deletar_contato.html
├── static/                # Arquivos estáticos
│   ├── css/
│   │   └── custom.css
│   └── js/
│       └── main.js
├── media/                 # Uploads (fotos)
├── db.sqlite3            # Banco de dados
└── manage.py             # Gerenciador Django
```

