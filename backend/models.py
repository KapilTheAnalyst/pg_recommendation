#from backend import models, schemas, crud, recommender
from sqlalchemy import Column , Integer , String , Float, Boolean
from .db import Base

class PG(Base):
    __tablename__ = "pgs" 

    id = Column(Integer , primary_key =True , index=True)
    name=Column(String, index=True)
    location =Column(String, index=True)
    price = Column(Float)
    gender= Column(String)
    amenities = Column(String, nullable = True)
    description=Column(String , nullable = True)
    room_type = Column(String, nullable = True)
    meals_included = Column(Boolean, nullable = True)



