from flask import Blueprint, request
from http import HTTPStatus
from sqlalchemy import inspect
from src.models import db, Post

bp = Blueprint("post", __name__, url_prefix="/posts")

# ... todas as rotas de criação, listagem, atualização e exclusão de posts
