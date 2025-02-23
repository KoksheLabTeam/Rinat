from typing import Sequence

from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete

from app.core.models.user import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, values: dict) -> User:
        query = insert(User).values(**values).returning(User)
        result = self.session.execute(query)
        self.session.commit()
        return result.scalar()

    def alter(self, values, **filters) -> User | None:
        query = update(User).filter_by(**filters).values(**values).returning(User)

        result = self.session.execute(query)
        self.session.commit()
        return result.scalar()

    def delete(self, **filters) -> None:
        query = delete(User).filter_by(**filters)

        self.session.execute(query)
        self.session.commit()

    def get_one(self, **filters) -> User | None:
        query = select(User).filter_by(**filters)

        result = self.session.execute(query)
        self.session.commit()

        return result.scalar()

    def get_all(self) -> Sequence[User]:
        query = select(User)

        result = self.session.execute(query)
        self.session.commit()
        return result.scalars().all()