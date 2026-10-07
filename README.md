# 🚀 ClearTask — Gerenciador de Tarefas Web

O **ClearTask** é uma aplicação web moderna e responsiva desenvolvida para organização e gestão de tarefas pessoais. O projeto conta com uma interface em **Dark Theme**, sistema completo de autenticação de utilizadores, suporte para foto de perfil e operações RESTful (CRUD) em tempo real.

---

## ✨ Funcionalidades

- **Autenticação & Sessão:**
  - Registo de utilizadores com encriptação de palavras-passe (`bcrypt`).
  - Login seguro com geração de tokens JWT armazenados em cookies HTTP-Only.
  - Tratamento automático de expiração de sessão (erro 401) com redirecionamento limpo para o login.

- **Dashboard Interativo:**
  - Métricas e estatísticas calculadas em tempo real (Total de Tarefas, Pendentes, Concluídas e Alta Prioridade).
  - Interface escura intuitiva com navegação por barra lateral.

- **Gestão de Tarefas (CRUD RESTful):**
  - Criação e edição de tarefas através de modal/pop-up dinâmico (`POST` / `PUT`).
  - Remoção de tarefas com modal de confirmação e requisição assíncrona (`DELETE`).
  - Organização por prioridades (Baixa, Média, Alta), status e data de vencimento.

- **Filtros e Pesquisa em Tempo Real:**
  - Filtro por abas (**Todas**, **Pendentes**, **Concluídas**) sem necessidade de recarregar a página.
  - Barra de pesquisa dinâmica que funciona em conjunto com a aba selecionada.

---

## 🛠️ Tecnologias Utilizadas

### **Backend**
- **Python 3.10+**
- **FastAPI**: Framework web assíncrono de alta performance.
- **SQLite3**: Banco de dados relacional leve.
- **Jinja2**: Motor de renderização de templates HTML.
- **PyJWT & Bcrypt**: Autenticação e segurança de palavras-passe.
- **python-multipart**: Processamento de uploads de ficheiros e formulários.

### **Frontend**
- **HTML5 & CSS3 Customizado**: Layout moderno adaptado para tema escuro.
- **JavaScript (Vanilla ES6+)**: Manipulação dinâmica do DOM e consumo de rotas REST via `Fetch API`.
- **FontAwesome**: Biblioteca de ícones da interface.

---

## 📁 Estrutura do Projeto

```text
ClearTask/
├── app/
│   ├── __pycache__/
│   ├── models/          # Modelos de dados / Pydantic
│   ├── routers/           # Rotas da API RESTful
│   ├── routes_html/      # Rotas de renderização de templates HTML
│   ├── schemas/          # Schemas Pydantic para validação de dados
│   ├── services/          # Regras de negócio e operações no banco
│   ├── static/           # Ficheiros estáticos (CSS, JS, imagens)
│   ├── templates/       # Templates HTML Jinja2 (dashboard, login, register)
│   ├── utils/            # Utilitários (tokens JWT, dependências, segurança)
│   ├── config.py         # Configurações globais da aplicação
│   ├── database.py        # Conexão e inicialização do SQLite
│   └── main.py           # Ponto de entrada da aplicação FastAPI
├── venv/                 # Ambiente virtual Python
├── .env                  # Variáveis de ambiente
├── .gitattributes
├── .gitignore
├── banco.db               # Ficheiro do banco de dados SQLite
└── requirements.txt       # Dependências do projeto


🔧 Como Executar o Projeto
Pré-requisitos
Python 3.10+ instalado.

Git instalado.

Passo a Passo
Clonar o repositório:

Bash
git clone [https://github.com/seu-usuario/cleartask.git](https://github.com/seu-usuario/cleartask.git)
cd cleartask
Criar e ativar o ambiente virtual (venv):

Bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
Instalar as dependências:

Bash
pip install -r requirements.txt
Iniciar o servidor com Uvicorn:

Bash
uvicorn main:app --reload
Aceder no navegador:
Abra o navegador e aceda a: http://127.0.0.1:8000/login

📝 Licença
Este projeto está sob a licença MIT. Sinta-se livre para o utilizar, estudar e modificar.


---

### Dica para o `requirements.txt`
Caso ainda não tenhas criado o ficheiro de dependências para o projeto, basta rodar este comando no teu terminal com o ambiente virtual ativo:

```bash
pip freeze > requirements.txt
