from typing import Sequence

from app.core.models.user import User
from app.core.schemas.user import UserCreate, UserUpdate
from app.core.repos.user import UserRepository


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def create(self, data: UserCreate) -> User:
        values: dict = data.model_dump()
        return self.repository.create(values)

    def update(self, data: UserUpdate, **filters) -> User:
        values = data.model_dump(exclude_none=True, exclude_unset=True)
        return self.repository.alter(values, **filters)

    def delete(self, **filters) -> None:
        return self.repository.delete(**filters)

    def get_one(self, **filters) -> User | None:
        return self.repository.get_one(**filters)

    def get_all(self) -> Sequence[User]:
        return self.repository.get_all()