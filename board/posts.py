from flask import (
    Blueprint,
    redirect,
    render_template,
    request,
    url_for,
)

from board.database import get_db

bp = Blueprint("posts",__name__)


@bp.route("/create", methods=("GET", "POST"))
def create():
    if request.method == 'POST':
        author = request.form['author'] or 'Anonymous spirit'
        message = request.form['message']

        if message:
            db = get_db()
            db.execute(
                'INSERT INTO post (author,message) VALUES (?,?)',
                (author, message),
            )
            db.commit()

    return render_template("posts/create.html")


@bp.route("/posts")
def posts():
    db = get_db()
    posts = db.execute(
        'SELECT author, message, created FROM post ORDER BY created DESC'
    ).fetchall()

    return render_template("posts/posts.html",posts=posts)