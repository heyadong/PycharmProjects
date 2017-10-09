from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(50))

engine = create_engine('mysql+mysqlconnector://root:password@localhost:3306/mytest')
DBSession = sessionmaker(bind=engine)
session = DBSession()
