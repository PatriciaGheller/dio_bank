from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# importa os modelos para ficarem disponíveis no pacote
from .user import User
from .role import Role
from .post import Post
