from typing import Optional
from datetime import date

from pydantic import BaseModel

class InsurancesRequest(BaseModel):
    """Schema for request body of insurance"""
    person_id: Optional[int] = None
    insurance_name: str
    policy_number: str
    coverage_details: str


class InsurancesUpdateRequest(BaseModel):
    """Schema for update body of insurance"""
    person_id: Optional[int] = None
    insurance_name: Optional[str] = None
    policy_number: Optional[str] = None
    coverage_details: Optional[str] = None
    status: Optional[int] = None