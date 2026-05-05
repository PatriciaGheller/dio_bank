# importa os modelos para ficarem disponíveis no pacote

from .base import db
from .user import User
from .role import Role
from .post import Post

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

__all__ = ['db', 'User', 'Role', 'Post']



