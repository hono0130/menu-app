import strawberry
from strawberry.scalars import JSON


@strawberry.type
class Menu:
    name: str
    ingredients: JSON