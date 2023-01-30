from pydantic import BaseModel


class UserSchema(BaseModel):
    id:int  
    name: str
    email:str
    password:str
    
    class config:
        orm_mode:True

class Login(BaseModel):
    email:str
    password:str

