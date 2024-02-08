from sqlalchemy import (
    Column,
    String,
    Integer
)
from sqlalchemy.orm import relationship

from .database import db


class User(db.Model):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False, unique=False)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(30), nullable=False, unique=True)

    posts = relationship("Post", back_populates="user")
