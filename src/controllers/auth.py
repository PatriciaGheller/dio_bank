from http import HTTPStatus
from flask import Blueprint, request
from flask_jwt_extended import create_access_token
from src .app import bcrypt
from src.models import db, User

bp = Blueprint('auth', __name__, url_prefix='/auth')

def _valid_password(password_hash, password_raw):
    return bcrypt.check_password_hash(password_hash, password_raw)


@bp.route("/login", methods=["POST"])
def login():
        """
    Autentica usuário
    ---
    tags:
      - auth
    requestBody:
      required: true
      content:
        application/json:
          schema:
            $ref: '#/components/schemas/Auth'
    responses:
      200:
        description: Login bem-sucedido
        content:
          application/json:
            schema:
              type: object
              properties:
                token:
                  type: string
      401:
        description: Credenciais inválidas
    """
        username = request.json.get("username", None)
        password = request.json.get("password", None)
        user = db.session.execute(db.select(User).filter_by(username=username)).scalar_one_or_none()
    
        if not user or not _valid_password(user.password, password):
            return {"msg": "Bad username or password"}, HTTPStatus.UNAUTHORIZED

        access_token = create_access_token(identity=str(user.id))
        return {'access_token': access_token}
