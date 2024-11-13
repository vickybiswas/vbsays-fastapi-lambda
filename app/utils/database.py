# Import necessary modules and classes
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker, declarative_base
from app.constant.settings import DATABASE_URL

# Database setup
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
print(DATABASE_URL, "DATABASE_URLLLLLLLLLLLLLLLLLLLLLLLLL")
Base = declarative_base()

# Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# End of File