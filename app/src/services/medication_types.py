from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from src.schemas.medication_types import MedicationTypesRequest, MedicationTypesUpdateRequest
from src.utils.ctes import MEDICATION_TYPES_ROW
from src.utils.helper import rows_to_dicts
from datetime import datetime


def get(db_session: Session):
    """Get All Medication Types"""
    try:
        query = text("SELECT * FROM medication_types")
        medication_types = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        medication_types = rows_to_dicts(medication_types, MEDICATION_TYPES_ROW)
        
        return medication_types

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def create(medication_type: MedicationTypesRequest, db_session: Session, payload):
    """Create Medication Type"""
    try:
        created_at = datetime.now()
        created_by = payload.get("id")

        data_medication_type = {
            "company_id": medication_type.company_id,
            "medication_name": medication_type.medication_name,
            "description": medication_type.description,
            "status": 1,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None
        }

        query = text("INSERT INTO medication_types (company_id, medication_name, description, status, created_at, created_by, updated_at, updated_by) VALUES (:company_id, :medication_name, :description, :status, :created_at, :created_by, :updated_at, :updated_by)")

        db_session.execute(query, data_medication_type)

        db_session.commit()

        return {"message": "Medication Type created successfully", "data": data_medication_type}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def update(medication_type: MedicationTypesUpdateRequest, db_session: Session, payload):
    """Update Medication Type"""
    try:
        updated_at = datetime.now()
        updated_by = payload.get("id")

        data_medication_type = {
            "company_id": medication_type.company_id,
            "medication_name": medication_type.medication_name,
            "description": medication_type.description,
            "status": medication_type.status,
            "updated_at": updated_at,
            "updated_by": updated_by
        }

        query = text("UPDATE medication_types SET company_id = :company_id, medication_name = :medication_name, description = :description, status = :status, updated_at = :updated_at, updated_by = :updated_by WHERE id = :id")

        db_session.execute(query, data_medication_type)

        db_session.commit()

        return {"message": "Medication Type updated successfully", "data": data_medication_type}
    
    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def delete(medication_type_id: int, db_session: Session):
    """Delete Medication Type"""
    try:
        query = text("DELETE FROM medication_types WHERE id = :id")
        db_session.execute(query, {"id": medication_type_id})

        db_session.commit()

        return {"message": "Medication Type deleted successfully"}
    
    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex