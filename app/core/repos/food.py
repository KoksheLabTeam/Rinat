from typing import Sequence


from sqlalchemy.orm import Session
from sqlalchemy import  insert,select,update,delete

from app.core.models.food import Foods

class FoodsRepository:
    def __init__(self, session: Session ):
        self.session = session

    def create(self,values: dict) -> Foods:
        query = insert(Foods).values(**values). returning(Foods)
        result = self.session.execute(query)
        self.session.commit()
        return result.scalar()


    def alter(self,values, **filters) -> Foods:
        query = update(Foods).filter_by(**filters).values(**values). returning(Foods)
        result = self.session.execute(query)
        self.session.commit()
        return result.scalar()

    def delete(self,id: int) -> None:
        query = delete(Foods).filter_by(id=id). returning(Foods)

        self.session.execute(query)
        self.session.commit()

    def get_one(self, **filters) -> Foods | None:
        query = select(Foods).filter_by(**filters)

        result = self.session.execute(query)
        self.session.commit()

        return result.scalar()

    def get_all(self) -> Sequence[Foods]:
        query = select(Foods)

        result = self.session.execute(query)
        self.session.commit()
        return result.scalars().all()








