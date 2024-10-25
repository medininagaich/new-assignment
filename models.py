from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Post(BaseModel):
    title: str = Field(..., max_length=200)
    content: str
    author: str = Field(..., max_length=50)
    created_at: Optional[datetime] = Field(default_factory=datetime.utcnow)

class PostUpdate(BaseModel):
    title: Optional[str] = Field(None, max_length=200)
    content: Optional[str]
    author: Optional[str] = Field(None, max_length=50)