# app/models/warehouse.py

from datetime import datetime, timezone
from sqlalchemy import Column
from sqlmodel import SQLModel, Field
from typing import Optional, Dict, Any

class BaseMixin(SQLModel):
    id: Optional[int] = Field(default=None, primary_key=True, index=True, description="Primary key for the collection")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    is_active: bool = Field(default=True, nullable=True)
    
    # Define the 'extras' field as a JSONB field using PostgreSQL's JSONB
    #extras: Optional[Dict[str, Any]] = Field(default={},sa_type=JSON, nullable=True)

# End of File