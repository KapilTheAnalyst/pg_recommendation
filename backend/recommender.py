from sqlalchemy.orm import Session
import models

def recommend_pgs(db:Session, location: str=None, max_price: int = None):
    query= db.query(models.PG)

    if location:
        query = query.filter(models.PG.location.ilike(f"%{location}%"))

    if max_price:
        query = query.filter(models.PG.price <= max_price)

    results = query.order_by(models.PG.price.asc()).all()

    return results