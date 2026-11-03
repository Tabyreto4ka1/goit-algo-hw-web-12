from sqlalchemy import Column, Integer, String, Boolean, func, Table
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

Base = declarative_base()


class Contact(Base):
    __tablename__="contacts"
    id = Column(Integer, primary_key=True)
    name=Column(String(20), nullable=False)
    last_name=Column(String(20), nullable=False)
    email=Column(String(30), nullable=False)
    phone_number=Column(String(15), nullable=False)
    birthday=Column(DateTime, nullable=False)
    additional=Column(String(500))
    user_id = Column('user_id', ForeignKey('users.id', ondelete='CASCADE'), default=None)
    user = relationship('User', backref="contacts")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username=Column(String(150),nullable=False, unique=True)
    email = Column(String(150), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    refresh_token = Column(String(255), nullable=True)



