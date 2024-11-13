from typing import Optional
from sqlmodel import SQLModel, Field
from app.model.task import TaskBase, Task

class TaskUpdate(TaskBase):
    is_active: Optional[bool] = Field(default=True)

class TaskRead(TaskBase):
    id: int
    is_active: Optional[bool] = Field(default=True)

class TasksRead(SQLModel):
    data: list[TaskRead]
    count: int

# End of File

#class StateCreate(StateBase):
#    name:str
#    pass