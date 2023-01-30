from fastapi import Depends
from sqlalchemy.orm import Session


from database import SessionLocal
from  model import get_db

from starlette.exceptions import HTTPException

from model import User
from schema import UserSchema,Login

def login(user_db:Login,db:SessionLocal=Depends(get_db)):
        return db.query(User).filter(User.email==user_db.email,User.password==user_db.password).first()

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()



def user_insert(user_db:UserSchema,db:Session=Depends(get_db)):
    try:
        user_data=User(id=user_db.id,name=user_db.name,email=user_db.email,password=user_db.password)
        db.add(user_data)
        db.commit()
        db.refresh(user_data)
        return user_data
    except:
        return HTTPException(status_code=404, detail="Already insert")


def update_data(user_db:UserSchema,db:SessionLocal=Depends(get_db)):
    try:
        user_update=db.query(User).filter(User.id==user_db.id).first()
        user_update.name=user_db.name
        user_update.email=user_db.email
        user_update.password=user_db.password
        db.add(user_update)
        db.commit()
        db.refresh(user_update)
        return user_update   
    except:
        return HTTPException(status_code=404)

def delete_data(id:int,db:SessionLocal=Depends(get_db)):
    try:
        user_delete=db.query(User).filter(User.id==id).first()
        db.delete(user_delete)
        db.commit()
        return (f"User of id {id} is Deleted Sucessfully")
    except:
        return HTTPException(status_code=404, detail="not found")        