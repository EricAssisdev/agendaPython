# 📇 Agenda Eletrônica - Django

Uma aplicação web moderna e intuitiva para gerenciar seus contatos pessoais e profissionais, desenvolvida com Django e Tailwind CSS.

## ✨ Características

### 🎨 Design Moderno
- Interface limpa e responsiva com Tailwind CSS
- Animações suaves e transições elegantes
- Ícones do Font Awesome
- Gradientes e efeitos visuais modernos
- Totalmente responsivo (mobile, tablet, desktop)

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
- Foto de perfil

#### Recursos Avançados
- 🔍 **Busca avançada** por nome, email, telefone ou empresa
- 🏷️ **Filtros** por categoria
- ⭐ **Filtro de favoritos**
- 📄 **Paginação** (12 contatos por página)
- 📊 **Dashboard** com estatísticas
- 🎨 **Avatares coloridos** com iniciais
- 📱 **Totalmente responsivo**

## 🚀 Como Usar

### Pré-requisitos
- Python 3.8 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Navegue até a pasta do projeto:**
```bash
cd C:\Users\Eric\Desktop\faculdade\python-app
```

2. **(Opcional) Instale o Pillow para upload de fotos:**
```bash
pip install Pillow
```

### Executar a Aplicação

1. **Inicie o servidor de desenvolvimento:**
```bash
python manage.py runserver
```

2. **Acesse no navegador:**
```
http://127.0.0.1:8000/
```

### Criar um Superusuário (Administrador)

Para acessar o painel administrativo do Django:

```bash
python manage.py createsuperuser
```

Depois acesse: `http://127.0.0.1:8000/admin/`

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

## 🎯 Funcionalidades Detalhadas

### Dashboard
- Total de contatos cadastrados
- Contador de favoritos
- Número de categorias
- Design com cards informativos

### Lista de Contatos
- Visualização em grid responsivo
- Cards com informações resumidas
- Avatares coloridos ou fotos
- Badge de categoria
- Ícone de favorito
- Busca e filtros integrados

### Detalhes do Contato
- Visualização completa de todas as informações
- Layout em colunas (principal + sidebar)
- Ações rápidas (editar, excluir, voltar)
- Informações do sistema (data de criação/atualização)
- Design elegante com ícones e cores

### Formulários
- Validação de campos
- Mensagens de erro claras
- Layout responsivo em grid
- Campos com ícones
- Preview de foto (JavaScript)
- Formatação automática de telefone

### Filtros e Busca
- Busca em tempo real
- Múltiplos filtros simultâneos
- Preservação de filtros na paginação
- Botão para limpar filtros

## 🎨 Tecnologias Utilizadas

- **Backend:** Django 5.2.8
- **Frontend:** HTML5, CSS3, JavaScript
- **Estilização:** Tailwind CSS (via CDN)
- **Ícones:** Font Awesome 6.4.0
- **Fontes:** Google Fonts (Inter)
- **Banco de Dados:** SQLite3

## 📱 Responsividade

A aplicação é totalmente responsiva e funciona perfeitamente em:
- 📱 Smartphones (320px+)
- 📱 Tablets (768px+)
- 💻 Desktops (1024px+)
- 🖥️ Telas grandes (1920px+)

## 🎨 Paleta de Cores

- **Primária:** Azul (#3B82F6) e Roxo (#9333EA)
- **Categorias:**
  - Família: Verde
  - Amigos: Azul
  - Trabalho: Roxo
  - Outros: Cinza
- **Ações:**
  - Sucesso: Verde
  - Erro: Vermelho
  - Aviso: Amarelo
  - Info: Azul

## 🔒 Segurança

- Proteção CSRF em todos os formulários
- Validação de dados no backend
- Confirmação antes de exclusões
- Mensagens de feedback para todas as ações

## 🌟 Melhores Práticas Implementadas

### UX/UI
- ✅ Feedback visual imediato
- ✅ Animações suaves
- ✅ Mensagens de sucesso/erro claras
- ✅ Confirmações para ações destrutivas
- ✅ Estados de hover e foco
- ✅ Hierarquia visual clara
- ✅ Consistência em toda aplicação

### Código
- ✅ Código organizado e modular
- ✅ Nomenclatura clara e descritiva
- ✅ Comentários explicativos
- ✅ Separação de responsabilidades
- ✅ DRY (Don't Repeat Yourself)
- ✅ Templates reutilizáveis

## 📝 Próximos Passos (Melhorias Futuras)

- [ ] Autenticação de usuários
- [ ] Exportar contatos (CSV, vCard)
- [ ] Importar contatos
- [ ] Grupos de contatos
- [ ] Tags personalizadas
- [ ] API REST
- [ ] Aplicativo mobile
- [ ] Sincronização com Google Contacts
- [ ] Backup automático
- [ ] Modo escuro

## 🤝 Contribuindo

Sinta-se à vontade para contribuir com melhorias!

## 📄 Licença

Este projeto é open source e está disponível para uso educacional.

## 👨‍💻 Desenvolvedor

Desenvolvido com ❤️ usando Django e Tailwind CSS

---

**Aproveite sua Agenda Eletrônica!** 🎉
