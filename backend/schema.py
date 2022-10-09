import strawberry
from strawberry.scalars import JSON


@strawberry.type
class Menu:
    name: str
    imageURL: str
    ingreds: JSON
    is_side: bool
    duration: int

    
