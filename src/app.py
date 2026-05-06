import os
import click
from flask import Flask, app, current_app
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from src.models.base import db

migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()

@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    with current_app.app_context():
        db.create_all()
    click.echo('Initialized the database.')

def create_app(environment=os.environ['ENVIRONMENT']):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(f'src.config.{environment.title()}Config')

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
    bcrypt.init_app(app)

    # Register blueprints
    from src.controllers import user, role, post, auth
    app.register_blueprint(user.bp)
    app.register_blueprint(role.bp)
    app.register_blueprint(post.bp)
    app.register_blueprint(auth.bp)

    return app
