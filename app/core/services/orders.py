from typing import Sequence

from app.core.models.orders import Orders
from app.core.schemas.orders import OrderCreate, OrderUpdate
from app.core.repos.orders import OrdersRepository


class UserService:
    def __init__(self, repository: OrdersRepository):
        self.repository = repository

    def create(self, data: OrderCreate) -> Orders:
        values: dict = data.model_dump()
        return self.repository.create(values)

    def update(self, data: OrderUpdate, **filters) -> Orders:
        values = data.model_dump(exclude_none=True, exclude_unset=True)
        return self.repository.alter(values, **filters)

    def delete(self, **filters) -> None:
        return self.repository.delete(**filters)

    def get_one(self, **filters) -> Orders | None:
        return self.repository.get_one(**filters)

    def get_all(self) -> Sequence[Orders]:
        return self.repository.get_all()