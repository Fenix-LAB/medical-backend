from datetime import date
from typing import Optional

from pydantic import BaseModel


class MedicationDietsRequest(BaseModel):
    """Schema for request body of medication_diets"""

    medication_type_id: int
    company_id: int
    medication_diet_name: str
    generic_composition: str
    indications: str
    contraindications: str


class MedicationDietsUpdateRequest(BaseModel):
    """Schema for update body of medication_diets"""

    medication_type_id: Optional[int] = None
    company_id: Optional[int] = None
    medication_diet_name: Optional[str] = None
    generic_composition: Optional[str] = None
    indications: Optional[str] = None
    contraindications: Optional[str] = None
    status: Optional[int] = None
