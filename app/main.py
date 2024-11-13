from fastapi import FastAPI
from app.route.main import api_router as router
from app.utils.server import settings

app = FastAPI()

@app.get("/")
async def main():
    return {"message": "This is the main page of the API"}

app.include_router(router, prefix=settings.API_PATH)



from sqlmodel import Field, SQLModel, create_engine
from app.constant.settings import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)

SQLModel.metadata.create_all(engine)
print("DATABASE_URLLLLLLLLLLLLLLLLLLLLLLLLL", DATABASE_URL) 
# End of File