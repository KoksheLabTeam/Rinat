from typing import Sequence

from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete

from app.core.models.orders import Orders


class OrdersRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, values: dict) -> Orders:
        query = insert(Orders).values(**values).returning(Orders)
        result = self.session.execute(query)
        self.session.commit()
        return result.scalar()

    def alter(self, values, **filters) -> Orders | None:
        query = update(Orders).filter_by(**filters).values(**values).returning(Orders)

        result = self.session.execute(query)
        self.session.commit()
        return result.scalar()

    def delete(self, **filters) -> None:
        query = delete(Orders).filter_by(**filters)

        self.session.execute(query)
        self.session.commit()

    def get_one(self, **filters) -> Orders | None:
        query = select(Orders).filter_by(**filters)

        result = self.session.execute(query)
        self.session.commit()

        return result.scalar()

    def get_all(self) -> Sequence[Orders]:
        query = select(Orders)

        result = self.session.execute(query)
        self.session.commit()
        return result.scalars().all()