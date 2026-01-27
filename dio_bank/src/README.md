# 📘 DIO Blog API 🏦
https://img.shields.io/badge/Python-3.12-blue?logo=python  
https://img.shields.io/badge/Flask-2.3-lightgrey?logo=flask  
https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=sqlite  
https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow

Uma aplicação desenvolvida em Flask para estudo de criação de APIs REST, com foco em usuários e posts.
O projeto foi construído durante práticas de desenvolvimento de APIs com Python e Flask.

# 🚀 Funcionalidades

### - CRUD de Usuários

 - Criar, listar, buscar, atualizar e deletar usuários

### - CRUD de Posts

- Criar, listar, buscar, atualizar e deletar posts

### - Relação entre Usuários ↔ Posts

- Cada post pertence a um usuário

- Cada usuário pode ter vários posts

### - Respostas enriquecidas:

- Posts retornam o author_username

- Usuários retornam seus posts

# 🛠️ Tecnologias utilizadas

- [Python 3.12](https://www.python.org/)

- [Flask](https://flask.palletsprojects.com/)

- [SQLAlchemy](https://www.sqlalchemy.org/)

- [SQLite](https://www.sqlite.org/)

- [Insomnia](https://insomnia.rest/)

# 📂 Estrutura do projeto

dio_bank/
│
├── src/
│   ├── app.py              # Configuração principal da aplicação Flask
│   ├── models.py           # Definição das classes User e Post
│   └── controllers/
│       ├── user.py         # Rotas e lógica de usuários
│       └── post.py         # Rotas e lógica de posts
│
└── README.md               # Documentação do projeto

# 🔗 Endpoints

## 👤 Usuários

- POST /users → cria usuário

- GET /users → lista todos os usuários (com posts)

- GET /users/<id> → busca usuário específico (com posts)

- PATCH /users/<id> → atualiza usuário

- DELETE /users/<id> → remove usuário

# 📝 Posts

- POST /posts → cria post vinculado a um usuário

- GET /posts → lista todos os posts (com nome do autor)

- GET /posts/<id> → busca post específico

- PATCH /posts/<id> → atualiza post

- DELETE /posts/<id> → remove post

# 📖 Exemplos de uso

### Criar usuário

POST /users
{
  "username": "Breno"
}

### Criar post

POST /posts
{
  "title": "Meu primeiro post",
  "body": "Estou aprendendo Flask!",
  "author_id": 2
}

### Listar usuários

GET /users
{
  "users": [
    {
      "id": 2,
      "username": "Breno",
      "posts": [
        {
          "id": 2,
          "title": "Meu primeiro post",
          "body": "Estou aprendendo Flask!",
          "created": "2026-01-27T21:31:53"
        }
      ]
    }
  ]
}

# 📌 Como rodar o projeto

1. Clone este repositório:

git clone https://github.com/seu-usuario/dio-bank-api.git
cd dio-bank-api

2. Crie o ambiente virtual com Poetry:

poetry install

3. Execute a aplicação:

flask run

4. Teste os endpoints com Insomnia ou cURL.

# 🎯 Próximos passos

- Adicionar comentários nos posts

- Implementar autenticação (JWT)

- Criar documentação automática com Swagger/OpenAPI

- Implementar paginação em listagens

# 👩‍💻 Autora

Projeto desenvolvido por Patrícia Gheller como parte dos estudos de desenvolvimento de APIs com Flask.

