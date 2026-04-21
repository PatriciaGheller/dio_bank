# Dio Bank API (Flask)

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey?logo=flask)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0-red?logo=sqlite)
![Status](https://img.shields.io/badge/Status-Em%20Desenvolvimento-yellow)

## 📌 Sobre o projeto
Aplicação backend desenvolvida em Flask para estudo de APIs REST, incluindo conexão com banco de dados SQLite e gerenciamento de migrações de banco de dados.

## 🔗 Links

- Repositório: [https://github.com/PatriciaGheller/Flask](https://github.com/PatriciaGheller/Flask)
- Documentação oficial do Flask: [https://flask.palletsprojects.com](https://flask.palletsprojects.com)

## 🚀 Tecnologias utilizadas

- Python 3.x
- Flask
- SQLite
- Poetry

## 🛠️ Ferramentas e bibliotecas

- Insomnia
- Flask‑Migrate (integração com Alembic para migrações de banco de dados)
- Pytest (framework de testes automatizados)

## 📂 Estrutura do projeto

Desenvolvimento-de-APIs-flask/
│
├── dio_bank/
│   ├── src/
│   │   ├── app.py          # Arquivo principal da aplicação Flask
│   │   ├── models.py       # Definição das tabelas/entidades
│   │   ├── utils.py        # Funções auxiliares
│   │   └── tests/          # Testes automatizados com pytest
│   │       └── test_utils.py
│   ├── migrations/         # Scripts de migração gerados pelo Flask-Migrate
│   └── init.py
│
├── README.md
├── pyproject.toml
├── poetry.lock
└── schema.sql

## ⚙️ Configuração do ambiente

1. Clone este repositório:

   ```bash
   git clone https://github.com/PatriciaGheller/flask.git

2. Instale as dependências com Poetry:
poetry install

## 🗄️ Banco de dados

O banco é inicializado com o comando:

poetry run flask --app dio_bank.src.app init-db

Crie e aplique migrações:

poetry run flask --app dio_bank.src.app db migrate -m "Mensagem da migração"
poetry run flask --app dio_bank.src.app db upgrade

O schema inicial está definido em schema.sql.

## ▶️ Executando a aplicação

Para rodar o servidor em modo debug:

poetry run flask --app dio_bank.src.app run --debug

A aplicação estará disponível em:
<http://127.0.0.1:5000>

## 📡 Endpoints principais

### Usuários

- GET /users → Lista todos os usuários

- POST /users → Cria um novo usuário

- GET /users/<id> → Detalhes de um usuário específico

- PUT /users/<id> → Atualiza dados de um usuário

- DELETE /users/<id> → Remove um usuário

### Posts

- GET /posts → Lista todos os posts

- POST /posts → Cria um novo post

- GET /posts/<id> → Detalhes de um post específico

- PUT /posts/<id> → Atualiza um post

- DELETE /posts/<id> → Remove um post

## 🧪 Testes

Os testes são escritos com pytest e ficam na pasta dio_bank/src/tests.

Para rodar todos os testes:

poetry run pytest

## 💻 Exemplo de uso

Criando um usuário via curl:

curl -X POST <http://127.0.0.1:5000/users> \
     -H "Content-Type: application/json" \
     -d '{"name": "Patricia", "email": "<patricia@example.com>"}'

Resposta esperada:

{
  "id": 1,
  "name": "Patricia",
  "email": "<patricia@example.com>"
}

## 📈 Próximos passos

- Implementar autenticação JWT ✅

- Criar documentação Swagger/OpenAPI

- Adicionar testes de integração

- Configurar CI/CD com GitHub Actions

## 👩‍💻 Autora

Projeto desenvolvido por Patrícia Gheller  
GitHub: <https://github.com/PatriciaGheller> (github.com in Bing)  
LinkedIn: <https://www.linkedin.com/in/patriciagheller> (linkedin.com in Bing)

## 📜 Licença

Este projeto é apenas para fins de estudo e aprendizado.

