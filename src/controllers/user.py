from http import HTTPStatus
from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import inspect
from models import db, User
from utils import requires_role

app = Blueprint('user', __name__, url_prefix='/users')

# ... todas as rotas de criação, listagem, atualização e exclusão de usuários
