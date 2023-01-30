from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from starlette.exceptions import HTTPException

from database import SessionLocal

from model import get_db
from schema import UserSchema,Login
import crud



router = APIRouter(
    prefix='/user',
    tags=['user'],
)

@router.post('/login',status_code=200)
def login(user_db:Login,db:SessionLocal=Depends(get_db)):
        user_log=crud.login(db=db , user_db=user_db)
        if user_log:
            return("Succesfully Login")
        if not user_log:
            raise HTTPException (status_code=404,detail=f"Invalide email or password")



@router.get("/{user_id}")
def user_show(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@router.post("/Insert",status_code=200)
def user_insert(user_db:UserSchema,db:Session=Depends(get_db)):
    return crud.user_insert(db=db, user_db=user_db)


@router.put("/Update")
def update_data(user_db:UserSchema,db:SessionLocal=Depends(get_db)):
    return crud.update_data(db=db, user_db=user_db)

@router.delete("/Delete{id}")
def delete_data(id:int,db:SessionLocal=Depends(get_db)):
    return crud.delete_data(db=db,id=id)
