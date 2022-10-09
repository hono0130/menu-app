import strawberry
from strawberry.scalars import JSON

from crawling import crawling


@strawberry.type
class Menu:
    name: str
    link: str
    imageURL: str
    duration: str
    is_side: bool
    tag: str
    ingreds: JSON





    
