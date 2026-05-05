# importa os modelos para ficarem disponíveis no pacote

from .models import db, User, Role, Post
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



