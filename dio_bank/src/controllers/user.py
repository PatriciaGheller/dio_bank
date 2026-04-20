from http import HTTPStatus

from flask import Blueprint, request
from dio_bank.src.app import User, db
from flask_jwt_extended import jwt_required
from dio_bank.src.utils import requires_role

from sqlalchemy import inspect

from dio_bank.src.controllers import post

app = Blueprint('user', __name__, url_prefix='/users')

def _create_user():
    data = request.json
    user= User(
        username=data['username'],
        password=data['password'],
        role_id=data['role_id'],
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
            'role' : {
                'id': user.role.id,
                'name': user.role.name
            },
            'posts': [ 
                { 
                    'id': post.id,  
                    'title': post.title, 
                    'body': post.body, 
                    'created': post.created.isoformat() if post.created else None, 
                } 
                for post in user.posts 
            ]
        } 
        for user in users 
    ]
    

@app.route('/', methods=['GET', 'POST'])
@jwt_required()
@requires_role('admin')
def list_or_create_user():
    
    user_id = get_jwt_identity()
    user = db.get_or_404(User, user_id)
    
    if user.role.name != 'admin':
        return {'message': 'User dont have access.'}, HTTPStatus.FORBIDDEN
    
    if request.method == 'POST':
        _create_user()
        return {'message': 'User created successfully'}, HTTPStatus.CREATED
    else:
        return {'users': _list_users()}
    
@app.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = db.session.get(User, user_id)
    if not user:
        return {'error': 'User not found'}, HTTPStatus.NOT_FOUND
    return {
        'id': user.id,
        'username': user.username,
        'posts': [ 
            { 
                'id': post.id, 
                'title': post.title, 
                'body': post.body, 
                'created': post.created.isoformat() if post.created else None,
        }
        for post in user.posts 
    ]
}
    
    
@app.route('/<int:user_id>', methods=['PATCH'])
def update_user(user_id):
    user = db.get_or_404(User, user_id)
    data = request.json

    mapper = inspect(User)
    for column in mapper.attrs:
        if column.key in data:
            setattr(user, column.key, data[column.key])
        db.session.commit()
        
    return {
        'id': user.id,
        'username': user.username,
        }
    
    
@app.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = db.get_or_404(User, user_id)
    db.session.delete(user)
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT
