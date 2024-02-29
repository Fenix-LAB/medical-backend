from typing import Optional
from datetime import date

from pydantic import BaseModel

class ExamTypesRequest(BaseModel):
    """Schema for request body of exam_types"""
    company_id: int
    exam_name: str
    description: Optional[str] = None
    status: int
    created_by: int
    updated_by: int


class ExamTypesUpdateRequest(BaseModel):
    """Schema for update body of exam_types"""
    company_id: Optional[int] = None
    exam_name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
    updated_by: Optional[int] = None