from connections.db import meta
from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.sql.sqltypes import Integer, String

users = Table('users', meta,
              Column('id', Integer, primary_key=True, autoincrement=True),
              Column('name', String(length=255)),
              Column('email', String(length=255)),
              Column('password', String(length=255))
              )
