import os

from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin
from flask import Flask, jason
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from src.models.base import db
from werkzeug.exceptions import HTTPException
from flask import current_app


migrate = Migrate()
jwt = JWTManager()
bcrypt = Bcrypt()
ma = Marshmallow()
spec = APISpec(
    title='DIO Bank',
    version= '1.0.0',
    asyncapi= '2.6.0',
    info=dict(description='DIO Bank API'),
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)

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
    ma.init_app(app)

    # Register blueprints
    from src.controllers import user, role, post, auth
    
    app.register_blueprint(user.bp)
    app.register_blueprint(role.bp)
    app.register_blueprint(post.bp)
    app.register_blueprint(auth.bp)
    
    @app.route('/docs')
    def docs():
        return spec.path(view=user.delete_user).path(view=user.get_user).to_dict()

    from flask import json
    from  werkzeug.exceptions import HTTPException

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response

        return app
