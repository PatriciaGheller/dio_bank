from http import HTTPStatus

from flask import Blueprint, request
from src.models import Role, db

bp = Blueprint('role', __name__, url_prefix='/roles')

@bp.route('/', methods=['POST'])
def create_role():
    data = request.json
    role = Role(name=data['name'])
    db.session.add(role)
    db.session.commit()
    return {'message': 'Role created'}, HTTPStatus.CREATED

@bp.route('/roles', methods=['GET'])
def list_roles():
        """
    Lista todas as roles
    ---
    tags:
      - role
    responses:
      200:
        description: Lista de roles
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/Role'
    """
        roles = Role.query.all()
        return {'roles': [role.name for role in roles]}
