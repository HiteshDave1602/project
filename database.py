from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine("sqlite:///User.db")
engine = create_engine("sqlite:///./Post.db")

SessionLocal = sessionmaker(autocommit=False,bind=engine)
session = SessionLocal()

Base = declarative_base()



