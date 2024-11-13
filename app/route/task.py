from fastapi import APIRouter
from app.model.task import Task
from app.utils.database import get_db
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException

router = APIRouter()

@router.get("/", response_model=Task)
async def read_item(Task_id: int, db: Session = Depends(get_db)):
    db_item = db.query(Task).filter(Task.id == Task_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item