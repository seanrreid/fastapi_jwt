from typing import Any
from sqlalchemy import Column, Integer, String, Date, ForeignKey, LargeBinary, UniqueConstraint
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import as_declarative, mapped_column

from db import engine
from pydantic import BaseModel

# Base = declarative_base()

@as_declarative()
class Base:
    id: Any
    __name__: str

    # to generate tablename from classname
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(225), unique=True)
    hashed_password = Column(String)

    UniqueConstraint("email", name="uq_user_email")

    # def __repr__(self):
    #     """Returns string representation of model instance"""
    #     return "<User {full_name!r}>".format(full_name=self.full_name)


class Links(Base):
    __tablename__ = "links"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    long_url = Column(String)
    short_url = Column(String)
    user_id =  mapped_column(ForeignKey("users.id"))


class LinksModel(BaseModel):
    title: str
    long_url: str
    short_url: str
    user_id: int
