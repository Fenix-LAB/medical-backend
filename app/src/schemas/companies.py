from typing import Optional
from datetime import date

from pydantic import BaseModel


class CompanyRequest(BaseModel):
    """Schema for request body of company"""
    commercial_name: str
    contact_person_id: Optional[int] = None
    status: int
    # created_at: date
    created_by: int
    # updated_at: date
    updated_by: int


class CompanyUpdateRequest(BaseModel):
    """Schema for update body of company"""
    commercial_name: Optional[str] = None
    contact_person_id: Optional[int] = None
    status: Optional[int] = None
    updated_by: Optional[int] = None