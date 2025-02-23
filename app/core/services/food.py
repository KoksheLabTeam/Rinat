from typing import Sequence

from app.core.models.food import Foods
from app.core.schemas.food import FoodCreate, FoodUpdate
from app.core.repos.food import FoodsRepository


class UserService:
    def __init__(self, repository: FoodsRepository):
        self.repository = repository

    def create(self, data: FoodCreate) -> Foods:
        values: dict = data.model_dump()
        return self.repository.create(values)

    def update(self, data: FoodCreate, **filters) -> Foods:
        values = data.model_dump(exclude_none=True, exclude_unset=True)
        return self.repository.alter(values, **filters)

    def delete(self, **filters) -> None:
        return self.repository.delete(**filters)

    def get_one(self, **filters) -> Foods | None:
        return self.repository.get_one(**filters)

    def get_all(self) -> Sequence[Foods]:
        return self.repository.get_all()