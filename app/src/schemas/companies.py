from typing import Optional
from datetime import date

from pydantic import BaseModel


class CompanyRequest(BaseModel):
    """Schema for request body of company"""
    commercial_name: str
    contact_person_id: Optional[int] = None
    status: int
    created_at: date
    created_by: int
    updated_at: date
    updated_by: int


class CompanyResponse(BaseModel):
    """Schema for response body of company"""
    company_id: int
    commercial_name: str
    contact_person_id: Optional[int]
    status: int
    created_at: date
    created_by: int
    updated_at: date
    updated_by: int