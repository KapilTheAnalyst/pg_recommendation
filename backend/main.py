from . import models, schemas, crud, recommender
from fastapi import FastAPI , Depends , HTTPException
from sqlalchemy .orm import Session
#import models , schemas , crud , recommender
from db import SessionLocal, engine




# create all database tables 
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title = "PG Recommendation API",
              description="Backend Service for Paying guest recommendation system",
              version ="1.0.0")


# Dependency: get DB session for each request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# PG crud Routes




# get all the pg
@app.get("/pg/", response_model=list[schemas.PG])
def list_pgs(db: Session= Depends(get_db)):
    return crud.get_all_pg(db)


# get 1 PG
@app.get("/pg/{pg_id}", response_model = schemas.PG)
def read_pg(pg_id : int , db:Session=Depends(get_db)):
    result = crud.get_pg(db, pg_id)
    if not result:
        raise HTTPException(status_code=404, detail="Pg not found")
    return result


# Post PG OR Create PG
@app.post("/pg/", response_model =schemas.PG)
def create_pg(pg: schemas.PGCreate, db:Session = Depends(get_db)):
    return crud.create_pg(db,pg)



# Delete PG
@app.delete("/pg/{pg_id}")
def delete_pg(pg_id:int , db:Session=Depends(get_db)):
    deleted = crud.delete_pg(db , pg_id)
    if not deleted:
        raise HTTPException(status_code=404,detail="PG not found")
    return{"message": " PG deleted successfully"}



# -------- Recommendation Route

@app.get("/recommend/", response_model=list[schemas.PG])
def recommend_pgs(
    location: str | None = None,
    max_price: int| None = None,
    db:Session = Depends(get_db)
):
    return recommender.recommend_pgs(db , location , max_price)


# -------------Root

@app.get("/")
def root():
    return {"message": "PG Recommender API running! "}

