from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.schemas.appointments import AppointmentRequest, AppointmentUpdateRequest
from src.utils.ctes import APPPOINTMENTS_ROW
from src.utils.helper import clean_dict, rows_to_dicts


def get(db_session: Session):
    """Get All Appointments"""
    try:
        query = text("SELECT * FROM appointments")
        appointments = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        appointments = rows_to_dicts(appointments, APPPOINTMENTS_ROW)

        return appointments

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def create(appointment: AppointmentRequest, db_session: Session, payload):
    """Create Appointment"""
    try:
        created_at = datetime.now()
        created_by = payload.get("id")

        data_appointment = {
            "patient_id": appointment.patient_id,
            "doctor_id": appointment.doctor_id,
            "insurance_id": appointment.insurance_id,
            "establishment_id": appointment.establishment_id,
            "appointment_date": appointment.appointment_date,
            "appointment_hours": appointment.appointment_hours,
            "duration_minutes": appointment.duration_minutes,
            "status": 1,
            "notes": appointment.notes,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None,
        }

        query = text(
            "INSERT INTO appointments (patient_id, doctor_id, insurance_id, establishment_id, appointment_date,appointment_hours, duration_minutes, status, notes, created_at, created_by, updated_at, updated_by) VALUES (:patient_id, :doctor_id, :insurance_id, :establishment_id, :appointment_date, :appointment_hours, :duration_minutes, :status, :notes, :created_at, :created_by, :updated_at, :updated_by)"
        )

        db_session.execute(query, data_appointment)

        data_appointment = clean_dict(data_appointment)

        db_session.commit()

        return {"message": "Appointment created successfully", "data": data_appointment}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def update(
    appointment_id: int, appointment: AppointmentUpdateRequest, db_session: Session, payload
):
    """Update Appointment"""
    try:
        updated_at = datetime.now()
        updated_by = payload.get("id")

        data_appointment = {
            "patient_id": appointment.patient_id,
            "doctor_id": appointment.doctor_id,
            "insurance_id": appointment.insurance_id,
            "establishment_id": appointment.establishment_id,
            "appointment_date": appointment.appointment_date,
            "appointment_hours": appointment.appointment_hours,
            "duration_minutes": appointment.duration_minutes,
            "status": appointment.status,
            "notes": appointment.notes,
            "updated_at": updated_at,
            "updated_by": updated_by,
        }

        query = text(
            "UPDATE appointments SET patient_id = :patient_id, doctor_id = :doctor_id, insurance_id = :insurance_id, establishment_id = :establishment_id, appointment_date = :appointment_date, appointment_hours = :appointment_hours duration_minutes = :duration_minutes, status = :status, notes = :notes, updated_at = :updated_at, updated_by = :updated_by WHERE appointment_id = :appointment_id"
        )

        db_session.execute(query, {**data_appointment, "appointment_id": appointment_id})

        data_appointment = clean_dict(data_appointment)

        db_session.commit()

        return {"message": "Appointment updated successfully", "data": data_appointment}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def delete(appointment_id: int, db_session: Session):
    """Delete Appointment"""
    try:
        query = text("DELETE FROM appointments WHERE appointment_id = :appointment_id")
        db_session.execute(query, {"appointment_id": appointment_id})
        db_session.commit()

        return {"message": "Appointment deleted successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
