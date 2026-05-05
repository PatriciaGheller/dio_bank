import os
import click
from flask import Flask, current_app
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from src.models import models 
db = models.db  # importa db e modelos

migrate = Migrate()
jwt = JWTManager()

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    with current_app.app_context():
        db.create_all()
    click.echo('Initialized the database.')

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI="sqlite:///blog.sqlite",
        JWT_SECRET_KEY='minha_chave_super_secreta_de_32_caracteres_ou_mais',
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Register cli commands
    app.cli.add_command(init_db_command)

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Register blueprints
    from src.controllers import user, role, post, auth
    app.register_blueprint(user.bp)
    app.register_blueprint(role.bp)
    app.register_blueprint(post.bp)
    app.register_blueprint(auth.bp)

    return app
