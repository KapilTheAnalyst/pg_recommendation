from sqlalchemy.orm import Session
import models , schemas

# Create PG
def create_pg(db:Session, pg :schemas.PGCreate):
    db_pg = models.PG(
        name = pg.name,
        location=pg.location,
        price = pg.price,
        gender = pg.gender,
        amenities = pg.amenities,
        description = pg.description,
        room_type = pg.room_type,
        meals_included = pg.meals_included
    )

    db.add(db_pg)
    db.commit()
    db.refresh(db_pg)
    return db_pg

# Get all the PG
def get_all_pg(db:Session, skip: int =0 ,limit: int = 100):
    return db.query(models.PG).offset(skip).limit(limit).all()


   
# Get 1 PG
def get_pg(db:Session , pg_id: int):
    return db.query(models.PG).filter(models.PG.id==pg_id).first()
 

# Update PG
def update_pg(db:Session , pg_id: int , pg_data: schemas.PGCreate):
    pg = db.query(models.PG).filter(models.PG.id==pg_id).first()
    if not pg:
        return None
    pg.name=pg_data.name
    pg.location = pg_data.location
    pg.price = pg_data.price
    pg.gender = pg_data.gender
    pg.amenities = pg_data.amenities
    pg.description = pg_data.description
    pg.room_type= pg_data.room_type
    pg.meals_included = "yes" if pg_data.meals_included else "no"


    db.commit()
    db.refresh(pg)
    return pg
    


# Delete the PG

def delete_pg(db:Session, pg_id:int):
   pg = db.query(models.PG).filter(models.PG.id == pg_id).first()
   if pg:
        db.delete(pg)
        db.commit()
        return True
   return False





