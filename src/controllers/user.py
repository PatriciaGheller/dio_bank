from http import HTTPStatus
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import inspect
from src.models import db, User
from src.utils import requires_role
from src.app import bcrypt

bp = Blueprint('user', __name__, url_prefix='/users')



def _create_user():
    data = request.get_json()
    user = User(
        username=data['username'],
        password=bcrypt.generate_password_hash(data['password']),  # Lembre-se de hash a senha em produção
        role_id=data.get('role_id')
    )
    db.session.add(user)
    db.session.commit()
    
    
def _list_users():
    query = db.select(User)
    users = db.session.execute(query).scalars()
    return [
        {
            'id': user.id,
            'username': user.username,
            'role_id': user.role_id
        } for user in users
    ]
    



