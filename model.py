from sqlalchemy import Column,Integer,String

from database import *

class User(Base):
    __tablename__="Users"
    id=Column(Integer,primary_key=True)
    name=Column(String(50))
    email = Column(String(100))
    password = Column(String(10))
    
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base.metadata.create_all(bind=engine)








