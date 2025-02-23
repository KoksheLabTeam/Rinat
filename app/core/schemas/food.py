from typing import Optional

from app.core.schemas.base import BaseSchema



class FoodRead(BaseSchema):
    name: str
    price: float
    description: str
    photo: str


class FoodCreate(BaseSchema):
    name: str
    price: float
    description: str
    photo: str


class FoodUpdate(BaseSchema):
    name: Optional[str] = None
    price: Optional[bool] = None
    description: Optional[str] = None
    photo: Optional[str] = None
