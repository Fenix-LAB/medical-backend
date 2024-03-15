from typing import Optional
from datetime import date

from pydantic import BaseModel


class ExamsRequest(BaseModel):
    """Schema for request body of exam"""
    exam_type_id: int
    company_id: int
    exam_name: str
    description: Optional[str] = None
    # status: int
    # created_by: int
    # updated_by: int


class ExamsUpdateRequest(BaseModel):
    """Schema for update body of exam"""
    exam_type_id: Optional[int] = None
    company_id: Optional[int] = None
    exam_name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
    # updated_by: Optional[int] = None