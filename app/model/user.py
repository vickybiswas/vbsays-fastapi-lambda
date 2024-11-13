#from app.utils import generate_unique_id
from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from app.model.mixin import BaseMixin

class UserBase(SQLModel):
    name: str = Field(default=None, index=True, nullable=False, description="Name of the user")
    phone: Optional[str] = Field(default=None, description="Phone number of the user")
    email: Optional[str] = Field(default=None, description="Email address of the user")
    
class User(BaseMixin, UserBase, table=True):
    #slug: str = Field(nullable=False)
    #shares: Optional[List["Share"]] = Relationship(back_populates="shares", sa_relationship_kwargs={"foreign_keys": "[Share.id]"})
    tasks: [List["Task"]] = Relationship(back_populates="creator", sa_relationship_kwargs={"foreign_keys": "[Task.id]"})   

# End of File