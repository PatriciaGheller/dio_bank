from src.app import create_app

# Cria a aplicação Flask usando a factory
app = create_app()

# O servidor (gunicorn, uwsgi, etc.) vai usar a variável `app`
