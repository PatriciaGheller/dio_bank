from http import HTTPStatus
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import inspect
from src.models.models import db, User
from src.utils import requires_role

bp = Blueprint('user', __name__, url_prefix='/users')

# ... todas as rotas de criação, listagem, atualização e exclusão de usuários
