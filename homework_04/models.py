import os
from sqlalchemy import String, ForeignKey, Column, false, Integer, Text
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker


PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://user:example@localhost:5432/blog"
DB_ECHO = False

class Base:
    id = Column(Integer, primary_key=True, nullable=False, unique=True)

async_engine = create_async_engine(url=PG_CONN_URI, echo=DB_ECHO)

Base = declarative_base(cls=Base)

Session = sessionmaker(
    bind=async_engine,
    expire_on_commit=False,
    class_=AsyncSession
)


class User(Base):
    __tablename__ = "users"
    name = Column(String(30), nullable=True, unique=False)
    username = Column(String(100), nullable=False, unique=True)
    email = Column(String(150), nullable=False, unique=True)
    posts = relationship(
        "Post",
        back_populates="user",
        uselist=True,
    )

    def __str__(self):
        return f"User(id = {self.id}, username={self.username!r}, email = {self.email})"

    def __repr__(self):
        return str(self)


class Post(Base):
    __tablename__ = "posts"
    title = Column(String(100), nullable=False, unique=True)
    body = Column(
        Text,
        nullable=False,
        unique=False,
        default="",
        server_default=false(),
    )
    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        unique=False,
        nullable=False,
    )
    user = relationship(
        "User",
        back_populates="posts",
        uselist=False
    )

    def __str__(self):
        return f"Post(id = {self.id}, title={self.title!r})"

    def __repr__(self):
        return str(self)