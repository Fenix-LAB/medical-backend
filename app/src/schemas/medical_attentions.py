from datetime import date
from typing import Optional

from pydantic import BaseModel


class MedicalAttentionRequest(BaseModel):
    """Schema for request body of medical attention"""

    appointment_id: Optional[int] = None
    establishment_id: Optional[int] = None
    doctor_id: Optional[int] = None
    service_id: Optional[int] = None
    insurance_id: Optional[int] = None
    company_id: Optional[int] = None
    attention_date: date
    symptoms: str
    diagnosis: str
    treatment: str
    current_condition: str
    evolution: str
    next_appointment_date: date


class MedicalAttentionUpdateRequest(BaseModel):
    """Schema for update body of medical attention"""

    appointment_id: Optional[int] = None
    establishment_id: Optional[int] = None
    doctor_id: Optional[int] = None
    service_id: Optional[int] = None
    insurance_id: Optional[int] = None
    company_id: Optional[int] = None
    attention_date: Optional[date] = None
    symptoms: Optional[str] = None
    diagnosis: Optional[str] = None
    treatment: Optional[str] = None
    current_condition: Optional[str] = None
    evolution: Optional[str] = None
    next_appointment_date: Optional[date] = None
    status: Optional[int] = None
