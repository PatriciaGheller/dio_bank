# Dio Bank API (Flask)

## 📌 Sobre o projeto
Aplicação backend desenvolvida em Flask para estudo de APIs REST, incluindo conexão com banco de dados SQLite.

## 🚀 Tecnologias utilizadas
- Python 3.x
- Flask
- Poetry
- SQLite

## ⚙️ Configuração do ambiente
1. Clone este repositório:
   ```bash
   git clone https://github.com/SEU-USUARIO/SEU-REPOSITORIO.git

2. Instale as dependências com Poetry:
poetry install

🗄️ Banco de dados
O banco é inicializado com o comando:
poetry run flask --app dio_bank.src.app init-db

O schema inicial está definido em schema.sql.
▶️ Executando a aplicação
Para rodar o servidor em modo debug:
poetry run flask --app dio_bank.src.app run --debug

A aplicação estará disponível em:
http://127.0.0.1:5000

📜 Licença
Este projeto é apenas para fins de estudo e aprendizado.

