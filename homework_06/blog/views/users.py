from flask import (
    Blueprint,
    render_template,
    request,
    flash,
    redirect,
    url_for
)
from sqlalchemy.exc import IntegrityError, DatabaseError
from werkzeug.exceptions import InternalServerError

from models import User, Post
from views.forms import UserForm
from models.database import db


users_app = Blueprint("users_app", __name__)


@users_app.route("/add/", methods=["GET", "POST"], endpoint="add_user")
def add_user():
    form = UserForm()
    if request.method == "GET":
        return render_template("users/add_user.html", form=form)

    if not form.validate_on_submit():
        return render_template("users/add_user.html", form=form), 400

    name = form.name.data
    username = form.username.data
    email = form.email.data

    user = User(name=name, username=username, email=email)
    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError:
        error_text = f"Could not add user {user.username!r}"
        form.form_errors.append(error_text)
        return render_template("users/add_user.html", form=form), 400

    except DatabaseError:
        raise InternalServerError(f"Could not create post {user.username!r}")

    flash(f"User {username} ({name}) is created", "success")
    url = url_for("users_app.add_user")
    return redirect(url)
