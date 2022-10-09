import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from strawberry.scalars import JSON
from crawling import crawling

from schema import Menu
from crawling import crawling



@strawberry.type
class Query:
    @strawberry.field
    def all_menu(self) -> list[str]:
        return crawling(1)


schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)