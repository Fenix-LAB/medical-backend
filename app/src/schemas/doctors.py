from typing import Optional
from datetime import date

from pydantic import BaseModel


class DoctorsRequest(BaseModel):
    """Schema for request body of doctor"""
    person_id: Optional[int] = None
    specialty_id: Optional[int] = None
    license_number: str
    # status: int
    company_id: Optional[int] = None


class DoctorsUpdateRequest(BaseModel):
    """Schema for update body of doctor"""
    person_id: Optional[int] = None
    specialty_id: Optional[int] = None
    license_number: Optional[str] = None
    status: Optional[int] = None
    company_id: Optional[int] = None
    # updated_by: Optional[int] = None