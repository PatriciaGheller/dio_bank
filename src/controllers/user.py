from http import HTTPStatus
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from sqlalchemy import inspect
from src.models import db, User
from src.utils import requires_role
from src.app import bcrypt
from src.views.user import CreateUserSchema, UserSchema



bp = Blueprint('user', __name__, url_prefix='/users')


def _create_user():
    user_schema = CreateUserSchema()
    
    try:
        data = user_schema.load(request.json)
    except ValidationError as exc:
        return exc.messages, HTTPStatus.UNPROCESSABLE_ENTITY
    
    user = User(
        username=data['username'],
        password=bcrypt.generate_password_hash(data['password']),  # Lembre-se de hash a senha em produção
        role_id=data.get('role_id')
    )
    db.session.add(user)
    db.session.commit()
    return {"msg": "User created"}, HTTPStatus.CREATED


@jwt_required()
@requires_role('admin')  
def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    users_schema = UserSchema(many=True)
    return users_schema.dump(users)

    
@bp.route('/', methods=['GET','POST'])
def list_or_create_users():
    if request.method == 'POST':
        return _create_user()    
    else:
        return {"users": _list_users()}
    
    
@bp.route('/<int:user_id>')
def get_user(user_id):
    """User detail view.
    ---
    get:
        tags:
            - User
      parameters:
        - in: path
          name: user_id
          schema: UserIdParameter
      responses:
        200:
          description: Sucessful operation
          content:
            application/json:
              schema: UserSchema
                
    """
    user = db.session.get(User, user_id)
    return {
        'id': user.id,
        'username': user.username,
    }
    
@app.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """User delete view.
    ---
    delete:
        tags:
            - User
        summary: Delete a user 
        description: Delete a user
      parameters:
        - in: path
          name: user_id
          schema: UserIdParameter
        responses:
            204:
                description: Successfully operation
            404:
                description: User not found
                
    """
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()
    return '', HTTPStatus.NO_CONTENT
    



