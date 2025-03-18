from fastapi.exceptions import HTTPException

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy.exc import (
    SQLAlchemyError,
    IntegrityError,
)

from app.api.api_v1.user import user_login
from app.core.models.user import User
from app.core.schemas.user import (
    UserCreate,
    UserUpdate
)

def create_user(session:Session,data:UserCreate,telegram_id:str)->User:
    user_data:dict = data.model_dump()
    user=User(**user_data, telegram_id=telegram_id)

    session.add(user)
    try:
        session.commit()
        session.refresh(user)


    except IntegrityError as e:
        session.rollback()
        raise HTTPException(
            status_code=400,
            detail="Пользователь с введенным логином уже существует"
        ) from e
    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=500,detail=f"Не удалось создать пользователя: {e}"

        )
    return user

def get_user_by_id(session:Session,id:int)->User:
    try:
        query = select(User).where(User.id == id)
        user = session.execute(query).scalar()
        if not user:
            raise HTTPException(status_code=404,detail="Пользователь не найден.")

    except SQLAlchemyError as e:
        raise HTTPException(status_code=500,detail=f"Ошибка при получении пользователя: {e}")

    return user

def get_all_users(session:Session)->list[User]:
    try:
        query = select(User)
        user = session.execute(query).scalar().all()

    except SQLAlchemyError as e:
        raise HTTPException(
            status_code=500,detail=f"Ошибка при получении списка пользователей: {e}"

        )

    return user

def update_user_by_id(session:Session,id:str,data:UserUpdate)->User:
    user = get_user_by_id(session,id)

    update_data:dict = data.model_dump(exclude_unset=True,exclude_none=True)
    for key,value in update_data.items():
        setattr(user,key,value)

    try:
        session.commit()
        session.refresh(user)

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=500,detail= f"Не удалось обновить пользователя: {e}"

        )
    return user

def set_inactive_by_id(session:Session,id:int)->User:
    user = get_user_by_id(session,id)

    try:
        user.is_active = False
        session.commit()

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Не удалось установить пользователя как неактивного: {e}",

        )
def delete_user_by_id(session:Session,id:int)->User:
    user = get_user_by_id(session,id)

    try:
        session.delete(user)
        session.commit()

    except SQLAlchemyError as e:
        session.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Не удалось удалить пользователя: {e}"
        )

