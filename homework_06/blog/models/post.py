from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey
)
from sqlalchemy.orm import relationship

from .database import db


class Post(db.Model):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=False)
    title = Column(String(100), nullable=False, unique=True)
    body = Column(String(500), nullable=False, unique=False)

    user = relationship("User", back_populates="posts")
