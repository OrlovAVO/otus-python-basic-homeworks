import os
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, declared_attr, sessionmaker, relationship

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:example@localhost/postgres"


class Base:
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    @declared_attr
    def id(self):
        return Column(Integer, primary_key=True)


engine = create_engine(url=PG_CONN_URI, echo=False)
async_engine = create_async_engine(url=PG_CONN_URI,
                                   echo=False,
                                   pool_size=20,
                                   max_overflow=10)
Base = declarative_base(cls=Base)
Base.metadata.bind = engine

Session = sessionmaker(
    bind=async_engine,
    class_=AsyncSession,
    expire_on_commit=False
)


class User(Base):
    name = Column(String(30), nullable=False)
    username = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)
    posts = relationship("Post",
                         back_populates="user",
                         uselist=True)

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}, username={self.username}, email={self.email})"

    def __repr__(self):
        return str(self)


class Post(Base):
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, unique=False)
    title = Column(String(100), nullable=False)
    body = Column(String(1_000), nullable=False)
    user = relationship("User",
                        back_populates="posts",
                        uselist=False)

    def __str__(self):
        return f"{self.__class__.__name__}(user_id={self.user_id}, title={self.title})"

    def __repr__(self):
        return str(self)
