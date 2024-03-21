from typing import Optional
from datetime import date

from pydantic import BaseModel


class MedicationTypesRequest(BaseModel):
    """Schema for request body of medication type"""
    company_id: Optional[int] = None
    medication_name: str
    description: str


class MedicationTypesUpdateRequest(BaseModel):
    """Schema for update body of medication type"""
    company_id: Optional[int] = None
    medication_name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
    # updated_by: Optional[int] = None