import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from strawberry.scalars import JSON
from crawling import crawling
from starlette.middleware.cors import CORSMiddleware

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
        return await crawling(num)


schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)

