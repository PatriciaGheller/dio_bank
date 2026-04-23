from flask import Blueprint, request
from dio_bank.src.app import Post, db
from http import HTTPStatus
from sqlalchemy import inspect

bp = Blueprint("post", __name__, url_prefix="/posts")

def _create_post():
    data = request.get_json()
    title = data.get("title")
    body = data.get("body")
    author_id = data.get("author_id")

    if not title or not body or not author_id:
        return {"error": "Campos 'title', 'body' e 'author_id' são obrigatórios"}, HTTPStatus.BAD_REQUEST

    post = Post(title=title, body=body, author_id=author_id)
    db.session.add(post)
    db.session.commit()
    return {"message": "Post created successfully"}, HTTPStatus.CREATED

def _list_posts():
    query = db.select(Post)
    posts = db.session.execute(query).scalars()
    return [
        {
            "id": post.id,
            "title": post.title,
            "body": post.body,
            "author_id": post.author_id,
            "author_username": post.author.username if post.author else None,
            "created": post.created.isoformat() if post.created else None,
        }
        for post in posts
    ]

@bp.route("/", methods=["GET", "POST"])
def list_or_create_post():
    if request.method == "POST":
        return _create_post()
    else:
        return {"posts": _list_posts()}

@bp.route("/<int:post_id>", methods=["GET"])
def get_post(post_id):
    post = db.session.get(Post, post_id)
    if not post:
        return {"error": "Post não encontrado"}, HTTPStatus.NOT_FOUND
    return {
        "id": post.id,
        "title": post.title,
        "body": post.body,
        "author_id": post.author_id,
        "author_username": post.author.username if post.author else None,
        "created": post.created.isoformat() if post.created else None,
    }

@bp.route("/<int:post_id>", methods=["PATCH"])
def update_post(post_id):
    post = db.session.get(Post, post_id)
    if not post:
        return {"error": "Post não encontrado"}, HTTPStatus.NOT_FOUND

    data = request.get_json()
    mapper = inspect(Post)
    for column in mapper.attrs:
        if column.key in data:
            setattr(post, column.key, data[column.key])
    db.session.commit()

    return {
        "id": post.id,
        "title": post.title,
        "body": post.body,
        "author_id": post.author_id,
        "created": post.created.isoformat() if post.created else None,
    }

@bp.route("/<int:post_id>", methods=["DELETE"])
def delete_post(post_id):
    post = db.session.get(Post, post_id)
    if not post:
        return {"error": "Post não encontrado"}, HTTPStatus.NOT_FOUND

    db.session.delete(post)
    db.session.commit()
    return "", HTTPStatus.NO_CONTENT
