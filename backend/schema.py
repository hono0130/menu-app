import strawberry
from strawberry.scalars import JSON


@strawberry.type
class Menu:
    name: str
    imageURL: str
    ingredients: JSON
    duration: int
