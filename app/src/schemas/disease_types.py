from typing import Optional

from pydantic import BaseModel

class DiseaseTypesRequest(BaseModel):
    """Schema for request body of disease_types"""
    disease_name: str
    description: Optional[str] = None
    status: int
    created_by: int
    updated_by: int


class DiseaseTypesUpdateRequest(BaseModel):
    """Schema for update body of disease_types"""
    disease_name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[int] = None
    updated_by: Optional[int] = None
