from pydantic import BaseModel
from typing import List
from model import Dress


class DressSchema(BaseModel):
    """ Dress representation
    """
    description: str = "Plisse Black Dress"
    size: str = "P"
    color: str(50) = "Red"
    price: float = 100.50


class GetDressSchema(BaseModel):
    """ Define how to retrieve a dress.
    """
    description: str = "Plisse Black Dress"


class AllDressesSchema(BaseModel):
    """ Define how to list all dresses persisted in database.
    """
    dresses: List[DressSchema]


def show_dress_list(dresses: List[Dress]):
    """ Return a dress representation according to DressViewSchema.
    """
    result = []
    for dress in dresses:
        result.append({
            "nome": dress.description,
            "size": dress.size,
            "color": dress.color,
            "price": dress.price,
        })

    return {"dresses": result}


class DressViewSchema(BaseModel):
    """ Define how the dress will be returned.
    """
    id: int = 1
    description: str = "Red Mid Dress"
    size: str = "L"
    color: str = "Green"
    price: float = 55.60


class DressRemoveSchema(BaseModel):
    """ Define how to remove a dress.
    """
    description: str


def show_dress(dress: Dress):
    """ Return a dress representation according to DressViewSchema.
    """
    return {
        "id": dress.id,
        "description": dress.description,
        "size": dress.size,
        "color": dress.color,
        "price": dress.price,
    }