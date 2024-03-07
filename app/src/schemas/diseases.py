from typing import Optional
from pydantic import BaseModel

class DiseaseRequest(BaseModel):
    """Schema for request body of disease"""
    disease_type_id: Optional[int] = None
    disease_code: str
    disease_name: str
    description: Optional[str] = None
    status: int
    created_by: int
    updated_by: int


class DiseaseUpdateRequest(BaseModel):
    """Schema for update body of disease"""
    disease_type_id: Optional[int] = None
    disease_code: Optional[str] = None
    disease_name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
    updated_by: Optional[int] = None