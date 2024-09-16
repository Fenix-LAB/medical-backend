from typing import Optional

from pydantic import BaseModel


class EstablishmentRequest(BaseModel):
    """Schema for request body of establishment"""

    company_id: Optional[int] = None
    establishment_name: str
    establishment_number: str
    address: str
    city: str
    country: str
    # status: int
    # created_by: int
    # updated_by: int


class EstablishmentUpdateRequest(BaseModel):
    """Schema for update body of establishment"""

    company_id: Optional[int] = None
    establishment_name: Optional[str] = None
    establishment_number: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    country: Optional[str] = None
    status: Optional[int] = None
    # updated_by: Optional[int] = None
