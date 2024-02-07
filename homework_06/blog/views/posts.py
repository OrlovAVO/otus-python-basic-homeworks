from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
)
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import InternalServerError

from models import User, Post
from views.forms import PostForm
from models.database import db


posts_app = Blueprint("posts_app", __name__)


@posts_app.route("/add/", methods=["GET", "POST"], endpoint="add_post")
def add_post():
    form = PostForm()
    if request.method == "GET":
        return render_template("posts/add_post.html", form=form)

    if not form.validate_on_submit():
        return render_template("posts/add_post.html", form=form), 400

    user = form.user.data
    title = form.title.data
    body = form.body.data

    user_obj = User.query.filter_by(username=user).first()

    if not user_obj:
        return f"User {user} not found in the database", 500

    post = Post(user=user_obj, title=title, body=body)
    db.session.add(post)

    try:
        db.session.commit()
    except IntegrityError:
        error_text = f"Could not create post {post.title!r}"
        form.form_errors.append(error_text)
        return render_template("posts/add_post.html", form=form), 400

    except DatabaseError:
        raise InternalServerError(f"Could not create post {post.title!r}")

    url = url_for("view_blog")
    return redirect(url)
