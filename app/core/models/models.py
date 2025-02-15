from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


Base = declarative_base()

engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)




class Foods(Base):
    __tablename__ = 'foods'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(String)
    description = Column(String)
    photo = Column(String)



class Orders(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    datetime = Column(String)
    address = Column(String)
    full_name = Column(String)
    status = Column(String)
    phone_number = Column(String)
    total_price = Column(String)


