from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class UserForm(FlaskForm):
    name = StringField(
        label="Name",
        name="name",
        validators=[DataRequired()]
    )
    username = StringField(
        label="Username",
        name="username",
        validators=[DataRequired()]
    )
    email = StringField(
        label="E-mail",
        name="email",
        validators=[DataRequired()]
    )
