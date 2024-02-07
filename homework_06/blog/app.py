from flask import Flask, render_template
from flask_migrate import Migrate

from views import posts_app
from views import users_app
from models import Post
from models.database import db


app = Flask(__name__)
app.config.from_pyfile('settings.py')
db.init_app(app)
migrate = Migrate(app, db, compare_type=True)

app.register_blueprint(posts_app, url_prefix="/posts")
app.register_blueprint(users_app, url_prefix="/users")


@app.route("/", endpoint="view_blog")
def view_blog():
    posts = Post.query.all()
    return render_template("view_blog.html", posts=posts)


if __name__ == "__main__":
    app.run(port=8000)
