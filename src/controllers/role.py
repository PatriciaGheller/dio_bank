from http import HTTPStatus
from flask import Blueprint, request
from src.models.models import db, Role, User

bp = Blueprint('role', __name__, url_prefix='/roles')

@bp.route('/', methods=['POST'])
def create_role():
    data = request.json
    role = Role(name=data['name'])
    db.session.add(role)
    db.session.commit()
    return {'message': 'Role created'}, HTTPStatus.CREATED
