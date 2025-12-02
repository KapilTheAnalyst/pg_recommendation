from . import models
import pandas as pd
from .db import SessionLocal, engine
#import models

# Make sure tables are created
models.Base.metadata.create_all(bind=engine)

# Load CSV
df = pd.read_csv(r"C:\Users\welcome\Downloads\pg_dataset.csv")

db = SessionLocal()

for _, row in df.iterrows():
    pg = models.PG(
        name=row["name"],
        location=row["location"],
        price=row["price"],
        gender=row["gender"],
        amenities=row.get("amenities"),
        description=row.get("description"),
        room_type=row.get("room_type"),
        meals_included = True if str(row.get("meals_included")).lower() in ["yes", "true", "1"] else False
    )
    db.add(pg)

db.commit()
db.close()
print("Data inserted successfully!")
