# app/crud/states.py

from typing import List, Optional
#from app.api.deps import SessionDep
from sqlmodel import select, func
from app.model import User
from app.schema import UserUpdate, UsersRead, UserRead
#from app.api.deps import CurrentUser
#from app.utils import get_slug
from datetime import datetime

def get_user(user_id: int) -> any:
    # Retrieve SKU by ID
    return db.get(State, state_id)

def get_user_by_slug(slug: str) -> Optional[User]:
    statement = select(User).where(User.slug == slug)
    return session.exec(statement).first()

def get_states(db: SessionDep, skip: int = 1, limit: int = 10, search: Optional[str] = None,sortfield: Optional[str] = None, sort: Optional[str] = 'desc')-> StatesRead:
    query = select(State)
    if search:
        search = f"%{search}%"
        query = query.where(
            (State.name.ilike(search)) |
            (State.slug.ilike(search))
        )
    offset = (skip - 1) * limit

    # Default to 'created_at' if sortfield is not passed
    sort_field = State.created_at

    # Check if sortfield is provided
    if sortfield:
        sort_fields = {
            'id': State.id,
            'name': State.name,
            'slug': State.slug,
        }
        # Use the provided sortfield if it exists, otherwise default to 'created_at'
        sort_field = sort_fields.get(sortfield, State.created_at)

    # Apply sorting order
    if sort == 'desc':
        query = query.order_by(sort_field.desc())
    else:
        query = query.order_by(sort_field.asc())

    count = db.exec(select(func.count()).select_from(query.subquery())).one()
    states = db.exec(query.offset(offset).limit(limit)).all()
   
    return StatesRead(data=states, count=count)

def create_state(db: SessionDep, state_in: StateCreate) -> any:
    create_data = state_in.model_dump(exclude_unset=True)
    # Additional data to be added
    create_data.update({"slug": get_slug(state_in.name)})
    db_state = State.model_validate(create_data)
    
    db.add(db_state)
    db.commit()
    db.refresh(db_state)
    return db_state

def update_state(db: SessionDep,state_id: int, state_in: StateUpdate) -> any:
    db_state=get_state(db=db, state_id=state_id)
    if not db_state : 
       raise None
    state_data = state_in.model_dump(exclude_unset=True)
    for key, value in state_data.items():
        setattr(db_state, key, value)
    if state_in.name:
        db_state.slug = get_slug(state_data["name"])        
    db_state.updated_at = datetime.utcnow()  # Update the updated_at field
    db.add(db_state)
    db.commit()
    db.refresh(db_state)
    return db_state

def delete_state(db: SessionDep, state_id: int) -> State:
    state = get_state(db=db, state_id=state_id)
    if not state : 
       return False
    db.delete(state)
    db.commit()
    return state
