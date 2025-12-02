from pydantic import BaseModel
from typing import Optional

class PGBase(BaseModel):
    name:str
    location : str
    price :float
    gender : str
    amenities : Optional[str]= None
    description :Optional[str] = None
    room_type : Optional[str]= None
    meals_included: Optional[bool] = None
class PGCreate(PGBase):
    pass 

class PG(PGBase):
    id:int

    class Config:
        orm_mode=True
