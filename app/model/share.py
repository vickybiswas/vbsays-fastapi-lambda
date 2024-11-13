#from app.utils import generate_unique_id
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from app.model.mixin import BaseMixin

from app.enum.model import Permission

class ShareBase(SQLModel):
    user_id: Optional[int] = Field(default=None, foreign_key="user.id", description="ID of the user who shared this task")
    task_id: Optional[int] = Field(default=None, foreign_key="task.id", description="ID of the task being shared")
    shared_with: Optional[int] = Field(default=None, foreign_key="user.id", description="ID of the user with whom the task is shared")
    
class Share(BaseMixin, ShareBase, table=True):
    #slug: str = Field(nullable=False)
    #user: Optional["User"] = Relationship(back_populates="user", sa_relationship_kwargs={"foreign_keys": "[Share.user_id]"})
    #task: Optional["Task"] = Relationship(back_populates="task", sa_relationship_kwargs={"foreign_keys": "[Share.task_id]"})
    #shared: Optional["User"] = Relationship(back_populates="shared_with", sa_relationship_kwargs={"foreign_keys": "[Share.shared_with]"})
    note: Optional[str] = Field(default=None, description="Note for the shared task")
    permission: Optional[Permission] = Field(default=Permission.READ, description="Permission level for the shared task") 

# End of File