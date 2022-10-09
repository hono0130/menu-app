from ftplib import all_errors
import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from strawberry.scalars import JSON
from crawling import crawling
from starlette.middleware.cors import CORSMiddleware

from schema import Menu, MenuWithIngreds
from crawling import crawling, crawling_ingreds

all_menu = []

from schema import Menu
from crawling import crawling

app = FastAPI()

origins = [
  "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@strawberry.type
class Query:

    @strawberry.field
    async def all_menu(self, num: int) -> list[Menu]:
        all_menu = await crawling(num)
        print(all_menu)
        return [Menu.marshal(menu["name"], menu["link"], menu["img"], menu["duration"], menu["is_side"], menu["tag"]) for menu in all_menu]
    
    @strawberry.field
    async def all_menu_with_ingreds(self) -> list[MenuWithIngreds]:
        print(all_menu)
        lst = await crawling_ingreds(all_menu)
        return [MenuWithIngreds.marshal(menu["name"], menu["link"], menu["img"], menu["duration"], menu["is_side"], menu["tag"], menu["ingreds"]) for menu in lst]



schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

