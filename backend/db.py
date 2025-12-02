from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
import os

# Database file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL= f"sqlite:///{os.path.join(BASE_DIR , 'pg.db')}"

# Create sqlalchemy engine
engine = create_engine(DATABASE_URL ,connect_args={"check_same_thread":False})

# Create configured "Session" class
SessionLocal = sessionmaker(autocommit=False , autoflush=False , bind=engine)

#Base class for models
Base = declarative_base()
