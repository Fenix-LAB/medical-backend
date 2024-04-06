from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from src.schemas.specialties import SpecialtyRequest, SpecialtyUpdateRequest
from src.utils.ctes import SPECIALTIES_ROW
from src.utils.helper import rows_to_dicts
from datetime import datetime


def get(db_session: Session):
    """Get All Specialties"""
    try:
        query = text("SELECT * FROM specialties")
        specialties = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        specialties = rows_to_dicts(specialties, SPECIALTIES_ROW)
        
        return specialties

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def create(specialty: SpecialtyRequest, db_session: Session, payload):
    """Create Specialty"""
    try:
        created_at = datetime.now()
        created_by = payload.get("id")

        data_specialty = {
            "company_id": specialty.company_id,
            "specialty_name": specialty.specialty_name,
            "status": 1,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None
        }

        query = text("INSERT INTO specialties (company_id, specialty_name, status, created_at, created_by, updated_at, updated_by) VALUES (:company_id, :specialty_name, :status, :created_at, :created_by, :updated_at, :updated_by)")

        db_session.execute(query, data_specialty)

        db_session.commit()

        return {"message": "Specialty created successfully", "data": data_specialty}
    
    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def update(specialty: SpecialtyUpdateRequest, db_session: Session, payload):
    """Update Specialty"""
    try:
        updated_at = datetime.now()
        updated_by = payload.get("id")

        data_specialty = {
            "company_id": specialty.company_id,
            "specialty_name": specialty.specialty_name,
            "status": specialty.status,
            "updated_at": updated_at,
            "updated_by": updated_by
        }

        query = text("UPDATE specialties SET company_id = :company_id, specialty_name = :specialty_name, status = :status, updated_at = :updated_at, updated_by = :updated_by WHERE id = :id")

        db_session.execute(query, data_specialty)

        db_session.commit()

        return {"message": "Specialty updated successfully", "data": data_specialty}
    
    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    


def delete(specialty_id: int, db_session: Session):
    """Delete Specialty"""
    try:
        query = text("DELETE FROM specialties WHERE id = :id")
        db_session.execute(query, {"id": specialty_id})

        db_session.commit()

        return {"message": "Specialty deleted successfully"}
    
    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex