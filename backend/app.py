import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from strawberry.scalars import JSON

from schema import Menu



@strawberry.type
class Query:
    @strawberry.field
    def menu(self) -> Menu:
        return Menu(name="Patrick", ingredients=JSON({"egg":3}))

schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)