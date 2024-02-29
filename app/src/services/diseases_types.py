from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from src.schemas.disease_types import DiseaseTypesRequest, DiseaseTypesUpdateRequest
from src.utils.ctes import DISEASE_TYPES_ROW
from src.utils.helper import rows_to_dicts
from datetime import datetime


def get(db_session: Session):
    """Get All Disease Types"""
    try:
        query = text("SELECT * FROM disease_types")
        disease_types = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        disease_types = rows_to_dicts(disease_types, DISEASE_TYPES_ROW)
        
        return disease_types

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def create(disease_type: DiseaseTypesRequest, db_session: Session):
    """Create Disease Type"""
    try:
        # Generate the current datetime
        created_at = datetime.now()
        updated_at = datetime.now()

        data_disease_type = {
            "disease_name": disease_type.disease_name,
            "description": disease_type.description,
            "status": disease_type.status,
            "created_at": created_at,
            "created_by": disease_type.created_by,
            "updated_at": updated_at,
            "updated_by": disease_type.updated_by
        }

        query = text("INSERT INTO disease_types (disease_name, description, status, created_at, created_by, updated_at, updated_by) VALUES (:disease_name, :description, :status, :created_at, :created_by, :updated_at, :updated_by)")

        db_session.execute(query, data_disease_type)

        db_session.commit()

        return {"message": "Disease Type created successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def update(disease_type: DiseaseTypesUpdateRequest, disease_type_id: int, db_session: Session):
    """Update Disease Type"""
    try:
        # Generate the current datetime
        updated_at = datetime.now()

        data_disease_type = {
            "disease_name": disease_type.disease_name,
            "description": disease_type.description,
            "status": disease_type.status,
            "updated_at": updated_at,
            "updated_by": disease_type.updated_by
        }

        query = text("UPDATE disease_types SET disease_name = :disease_name, description = :description, status = :status, updated_at = :updated_at, updated_by = :updated_by WHERE id = :id")

        db_session.execute(query, {**data_disease_type, "id": disease_type_id})

        db_session.commit()

        return {"message": "Disease Type updated successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def delete(disease_type_id: int, db_session: Session):
    """Delete Disease Type"""
    try:
        query = text("DELETE FROM disease_types WHERE id = :id")
        db_session.execute(query, {"id": disease_type_id})
        db_session.commit()
        return {"message": "Disease Type deleted successfully"}
    
    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    