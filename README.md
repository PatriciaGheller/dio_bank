# 📘 DIO Bank API 🏦

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey?logo=flask)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=sqlite)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

API desenvolvida em Flask para estudo de criação de APIs REST, com foco em usuários, roles e posts.  
O projeto foi construído durante práticas de desenvolvimento de APIs com Python e Flask.

---

## 🚀 Funcionalidades

- CRUD de Usuários  
- CRUD de Roles  
- CRUD de Posts  
- Relação entre Usuários ↔ Roles ↔ Posts  
- Respostas enriquecidas (posts retornam `author_username`, usuários retornam seus posts)  
- Migrations com Alembic & Flask-Migrate  

---

## 🛠️ Tecnologias utilizadas

- [Python 3.12](https://www.python.org/)  
- [Flask](https://flask.palletsprojects.com/)  
- [SQLAlchemy](https://www.sqlalchemy.org/)  
- [PostgreSQL](https://www.postgresql.org/)  
- [Insomnia](https://insomnia.rest/)  
- [Alembic](https://alembic.sqlalchemy.org/)  
- [Flask-Migrate](https://flask-migrate.readthedocs.io/)
- - [Render](https://render.com/) → plataforma de deploy em nuvem. Permite **publicar aplicações Flask** e acessá-las remotamente por um endereço de servidor. Ideal para colocar produtos em produção e disponibilizar para todos.
- [DBeaver](https://dbeaver.io/) → ferramenta de administração de banco de dados. Usada para **visualizar, editar e gerenciar** o PostgreSQL da aplicação.

---

## 🌐 Deploy

A aplicação está publicada no **Render** e pode ser acessada remotamente pelo seguinte endereço:

👉 [Acessar aplicação](https://dio-bank-868m.onrender.com)

---

## 📂 Estrutura do projeto

dio_bank/
│
├── src/
│   ├── app.py              # Configuração principal da aplicação Flask
│   ├── wsgi.py             # Ponto de entrada WSGI
│   ├── utils.py            # Funções auxiliares
│   ├── models/             # Definição das classes User, Role e Post
│   │   ├── user.py
│   │   ├── role.py
│   │   └── post.py
│   └── controllers/        # Rotas e lógica de negócio
│       ├── auth.py
│       ├── user.py
│       ├── role.py
│       └── post.py
│
├── migrations/             # Controle de versão do banco (Alembic)
├── tests/                  # Testes de integração
└── README.md               # Documentação do projeto

---

## 🔗 Endpoints

### 👤 Usuários

- `POST /users` → cria usuário  
- `GET /users` → lista todos os usuários (com posts)  
- `GET /users/<id>` → busca usuário específico (com posts)  
- `PATCH /users/<id>` → atualiza usuário  
- `DELETE /users/<id>` → remove usuário  

### 📝 Posts

- `POST /posts` → cria post vinculado a um usuário  
- `GET /posts` → lista todos os posts (com nome do autor)  
- `GET /posts/<id>` → busca post específico  
- `PATCH /posts/<id>` → atualiza post  
- `DELETE /posts/<id>` → remove post  

### 🔑 Roles

- `POST /roles` → cria role  
- `GET /roles` → lista roles  
- `GET /roles/<id>` → busca role específica  
- `PATCH /roles/<id>` → atualiza role  
- `DELETE /roles/<id>` → remove role  

---

## 📖 Exemplos de uso

### Criar role

http
POST /roles
{
  "name": "admin"
}

### Criar usuário


POST /users
{
  "username": "Breno",
  "password": "123mudar",
  "active": true,
  "role_id": 1
}

## Criar post

POST /posts
{
  "title": "Meu primeiro post",
  "body": "Estou aprendendo Flask!",
  "author_id": 2
}

## 📌 Como rodar o projeto

1. Clone este repositório:

git clone https://github.com/seu-usuario/dio-bank-api.git
cd dio-bank-api

2. Crie o ambiente virtual com Poetry:

poetry install

3. Configure variáveis de ambiente (exemplo em .env):

FLASK_APP=src/app.py
FLASK_ENV=development
DATABASE_URL=postgresql://usuario:senha@localhost:5432/diobank

4. Inicialize o banco:

poetry run flask --app src/app db migrate -m "cria tabelas iniciais"
poetry run flask --app src/app db upgrade

5. Execute a aplicação:

poetry run flask --app src/app run

## 🎯 Próximos passos

- Adicionar comentários nos posts

- Implementar autenticação (JWT)

- Implementar autorização (controle de acesso por usuário/role)

- Criar documentação automática com Swagger/OpenAPI

- Implementar paginação em listagens

## 👩‍💻 Autora

Projeto desenvolvido por Patrícia Gheller como parte dos estudos de desenvolvimento de APIs com Flask.
