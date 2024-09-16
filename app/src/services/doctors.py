from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.schemas.doctors import DoctorsRequest, DoctorsUpdateRequest
from src.utils.ctes import DOCTORS_ROW
from src.utils.helper import clean_dict, rows_to_dicts


def get(db_session: Session):
    """Get All Doctors"""
    try:
        query = text("SELECT * FROM doctors")
        doctors = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        doctors = rows_to_dicts(doctors, DOCTORS_ROW)

        return doctors

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def create(doctor: DoctorsRequest, db_session: Session, payload):
    """Create Doctor"""
    try:
        created_at = datetime.now()
        created_by = payload.get("id")

        data_doctor = {
            "person_id": doctor.person_id,
            "specialty_id": doctor.specialty_id,
            "license_number": doctor.license_number,
            "company_id": doctor.company_id,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None,
        }

        query = text(
            "INSERT INTO doctors (person_id, specialty_id, license_number, company_id, created_at, created_by, updated_at, updated_by) VALUES (:person_id, :specialty_id, :license_number, :company_id, :created_at, :created_by, :updated_at, :updated_by)"
        )

        db_session.execute(query, data_doctor)

        db_session.commit()

        data_doctor = clean_dict(data_doctor)

        return {"message": "Doctor created successfully", "data": data_doctor}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def update(doctor_id: int, doctor: DoctorsUpdateRequest, db_session: Session, payload):
    """Update Doctor"""
    try:
        updated_at = datetime.now()
        updated_by = payload.get("id")

        data_doctor = {
            "person_id": doctor.person_id,
            "specialty_id": doctor.specialty_id,
            "license_number": doctor.license_number,
            "status": doctor.status,
            "company_id": doctor.company_id,
            "updated_at": updated_at,
            "updated_by": updated_by,
        }

        query = text(
            "UPDATE doctors SET person_id = :person_id, specialty_id = :specialty_id, license_number = :license_number, status = :status, company_id = :company_id, updated_at = :updated_at, updated_by = :updated_by WHERE doctor_id = :doctor_id"
        )

        db_session.execute(query, {**data_doctor, "doctor_id": doctor_id})

        db_session.commit()

        data_doctor = clean_dict(data_doctor)

        return {"message": "Doctor updated successfully", "data": data_doctor}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def delete(doctor_id: int, db_session: Session):
    """Delete Doctor"""
    try:
        query = text("DELETE FROM doctors WHERE doctor_id = :doctor_id")
        db_session.execute(query, {"doctor_id": doctor_id})

        db_session.commit()

        return {"message": "Doctor deleted successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
