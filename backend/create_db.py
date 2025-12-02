from backend import models, schemas, crud, recommender
from db import Base, engine
import models

# create all database tables 
Base.metadata.create_all(bind=engine)

print("Tables created")
