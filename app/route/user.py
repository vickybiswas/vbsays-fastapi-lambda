# app/api/states.py

# from app.my_enum.permission import PermissionActionStringEnum
# from app.decorators.auth import authorize
from fastapi import APIRouter, Response, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from app.model.user import User, UserBase
from app.schema.user import UserUpdate, UserRead, UsersRead
# from app import crud
# from app.api.deps import CurrentUser,SessionDep
# from app.utils import get_slug

router = APIRouter()

@router.post("/", response_model=User)
def create_state() -> any:
    #slug = get_slug(state_in.name)
    save = crud.create_state(db=db, state_in=state_in)
    if not save:
        raise HTTPException(
            status_code=400,
            detail="The state with this slug already exists in the system.",
        )
    return save

@router.get("/", response_model=UserRead)
def read_states(
    skip: int = 1,
    limit: int = 100,
    search: Optional[str] = None,
    sortfield: Optional[str] = None,
    sort: Optional[str] = 'desc'
) -> any:
    return crud.get_states(db=db, skip=skip, limit=limit,search=search,sortfield=sortfield,sort=sort)

