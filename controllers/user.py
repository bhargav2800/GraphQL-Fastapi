from fastapi import APIRouter
from strawberry.asgi import GraphQL

from connections.db import conn
from models.user import users
import strawberry

from type.user import Query, Mutation

user = APIRouter()
schema = strawberry.Schema(Query, Mutation)
graphql_app = GraphQL(schema)
user.add_route('/graphql', graphql_app)