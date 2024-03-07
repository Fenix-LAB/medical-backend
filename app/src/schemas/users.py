from typing import Optional
from pydantic import BaseModel


class UserRequest(BaseModel):
    """Schema for request body of user"""
    username: str
    password: str
    email: str
    full_name: str
    role: str
    status: int
    created_by: int
    updated_by: int


class UserUpdateRequest(BaseModel):
    """Schema for update body of user"""
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[str] = None
    full_name: Optional[str] = None
    role: Optional[str] = None
    status: Optional[int] = None
    updated_by: Optional[int] = None