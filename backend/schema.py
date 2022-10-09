import strawberry
from strawberry.scalars import JSON

@strawberry.type
class Menu:
    name: str
    link: str
    imageURL: str
    duration: str
    is_side: bool
    tag: str

    @classmethod
    def marshal(cls, name, link, imageURL, duration, is_side, tag):
        return cls(
            name=name, 
            link=link, 
            imageURL=imageURL, 
            duration=duration, 
            is_side=is_side, 
            tag=tag, 
        )

@strawberry.type
class MenuWithIngreds(Menu):
    ingreds: JSON

    @classmethod
    def marshal(cls, name, link, imageURL, duration, is_side, tag, ingreds):
        return cls(
            name=name, 
            link=link, 
            imageURL=imageURL, 
            duration=duration, 
            is_side=is_side, 
            tag=tag, 
            ingreds=ingreds,
        )    


    





    
