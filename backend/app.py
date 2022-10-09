import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from strawberry.scalars import JSON
from crawling import crawling

from schema import Menu
from crawling import crawling


ALL_MENU = []

@strawberry.type
class Query:
    @strawberry.field
    async def all_menu(self, num: int) -> list[Menu]:
        ALL_MENU = await crawling(num)
        return [Menu.marshal(menu["name"], menu["link"], menu["img"], menu["duration"], menu["is_side"], menu["tag"]) for menu in ALL_MENU]

print(ALL_MENU)

schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

