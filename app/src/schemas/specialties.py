from datetime import date
from typing import Optional

from pydantic import BaseModel


class SpecialtyRequest(BaseModel):
    """Schema for request body of specialty"""

    company_id: Optional[int] = None
    specialty_name: str


class SpecialtyUpdateRequest(BaseModel):
    """Schema for update body of specialty"""

    company_id: Optional[int] = None
    specialty_name: Optional[str] = None
    status: Optional[int] = None
