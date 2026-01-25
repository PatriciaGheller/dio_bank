from flask import Blueprint

bp = Blueprint("post", __name__, url_prefix="/posts")

@bp.route("/")
def index():
    return "Lista de posts"
