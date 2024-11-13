from typing import Optional
from sqlmodel import SQLModel, Field
from app.model.user import UserBase, User

class UserUpdate(UserBase):
    is_active: Optional[bool] = Field(default=True)

class UserRead(UserBase):
    id: int
    is_active: Optional[bool] = Field(default=True)

class UsersRead(SQLModel):
    data: list[UserRead]
    count: int

# End of File

#class StateCreate(StateBase):
#    name:str
#    pass