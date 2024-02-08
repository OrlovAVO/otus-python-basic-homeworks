from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    user = StringField(
        label="Username",
        name="username",
        validators=[DataRequired()]
    )
    title = StringField(
        label="Title",
        name="title",
        validators=[DataRequired()]
    )
    body = StringField(
        label="Post",
        name="body",
        validators=[DataRequired()]
    )
