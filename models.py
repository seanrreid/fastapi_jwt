from typing import Any
from sqlalchemy import Column, Integer, String, Date, ForeignKey
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


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)