from typing import Optional
from datetime import date

from pydantic import BaseModel


class PatientRequest(BaseModel):
    """Schema for request body of patient"""
    person_id: Optional[int] = None
    category: str
    occupation_ref: str
    income_date: date
    is_client: bool
    insurance: str
    alert_1: str
    alert_2: str
    alert_3: str
    company_id: Optional[int] = None


class PatientUpdateRequest(BaseModel):
    """Schema for update body of patient"""
    person_id: Optional[int] = None
    category: Optional[str] = None
    occupation_ref: Optional[str] = None
    income_date: Optional[date] = None
    is_client: Optional[bool] = None
    insurance: Optional[str] = None
    status: Optional[int] = None
    alert_1: Optional[str] = None
    alert_2: Optional[str] = None
    alert_3: Optional[str] = None
    company_id: Optional[int] = None
    # updated_by: Optional[int] = None