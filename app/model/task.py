#from app.utils import generate_unique_id
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from datetime import datetime
from app.model.mixin import BaseMixin

from app.enum.model import State

class TaskBase(SQLModel):
    user_id: Optional[int] = Field(default=None, foreign_key="user.id", description="ID of the user who shared this task")
    detail: str = Field(nullable=False, description="Details of the task")
    created_at: Optional[datetime] = Field(default=datetime.utcnow, description="Date and time when the task was created")
    changed_at: Optional[datetime] = Field(default=datetime.utcnow, description="Date and time when the task was last changed")
    state: Optional[State] = Field(default=State.PENDING, description="State of the task")     

class Task(BaseMixin, TaskBase, table=True):
    #slug: str = Field(nullable=False)
    creator: Optional["User"] = Relationship(back_populates="tasks", sa_relationship_kwargs={"foreign_keys": "[User.id]"})
    #shares: Optional[List["Share"]] = Relationship(back_populates="shares", sa_relationship_kwargs={"foreign_keys": "[Share.id]"})

# End of File