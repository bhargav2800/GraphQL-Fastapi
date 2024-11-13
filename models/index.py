from connections.db import engine, meta
from models.user import users

meta.create_all(engine)
