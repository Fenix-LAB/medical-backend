from typing import Optional
from datetime import date

from pydantic import BaseModel

class PersonsRequest(BaseModel):
    """Schema for request body of persons"""
    first_name: str
    last_name: str
    identification_type: int
    identification: str
    birthdate: date
    gender: str
    marital_status: str
    address: str
    phone_number: str
    email: str
    # created_at: date
    # created_by: int
    # updated_at: date
    # updated_by: int
    company_id: Optional[int]
    person_id: Optional[int] = None

class PersonsUpdateRequest(BaseModel):
    """Schema for update body of persons"""
    first_name: Optional[str]
    last_name: Optional[str]
    identification_type: Optional[int]
    identification: Optional[str]
    birthdate: Optional[date]
    gender: Optional[str]
    marital_status: Optional[str]
    address: Optional[str]
    phone_number: Optional[str]
    email: Optional[str]
    # created_at: Optional[date]
    # created_by: Optional[int]
    # updated_at: Optional[date]
    # updated_by: Optional[int]
    company_id: Optional[int]