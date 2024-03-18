from typing import Optional
from datetime import date

from pydantic import BaseModel

class AppointmentRequest(BaseModel):
    """Schema for request body of appointment"""
    patient_id: Optional[int] = None
    doctor_id: Optional[int] = None
    insurance_id: Optional[int] = None
    establishment_id: Optional[int] = None
    appointment_date: date
    duration_minutes: int
    # status: int
    notes: Optional[str] = None


class AppointmentUpdateRequest(BaseModel):
    """Schema for update body of appointment"""
    patient_id: Optional[int] = None
    doctor_id: Optional[int] = None
    insurance_id: Optional[int] = None
    establishment_id: Optional[int] = None
    appointment_date: Optional[date] = None
    duration_minutes: Optional[int] = None
    status: Optional[int] = None
    notes: Optional[str] = None