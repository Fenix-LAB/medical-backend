from typing import Optional

from pydantic import BaseModel


class ServiceRequest(BaseModel):
    """Schema for request body of service"""

    service_name: str
    description: Optional[str] = None
    price: float
    iva_percentage: float
    # status: int
    # created_by: int
    # updated_by: int
    company_id: Optional[int] = None
    specialty_id: Optional[int] = None


class ServiceUpdateRequest(BaseModel):
    """Schema for update body of service"""

    service_name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    iva_percentage: Optional[float] = None
    status: Optional[int] = None
    # updated_by: Optional[int] = None
    company_id: Optional[int] = None
    specialty_id: Optional[int] = None
