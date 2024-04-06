from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from src.schemas.diseases import DiseaseRequest, DiseaseUpdateRequest
from src.utils.ctes import DISEASES_ROW
from src.utils.helper import rows_to_dicts
from datetime import datetime


def get(db_session: Session):
    """Get All Diseases"""
    try:
        query = text("SELECT * FROM diseases")
        diseases = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        diseases = rows_to_dicts(diseases, DISEASES_ROW)
        
        return diseases

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def create(disease: DiseaseRequest, db_session: Session, token):
    """Create Disease"""
    try:
        # Generate the current datetime
        created_at = datetime.now()
        created_by = token.get("id")

        data_disease = {
            "disease_type_id": disease.disease_type_id,
            "disease_code": disease.disease_code,
            "disease_name": disease.disease_name,
            "description": disease.description,
            "status": 1,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None
        }

        query = text("INSERT INTO diseases (disease_type_id, disease_code, disease_name, description, status, created_at, created_by, updated_at, updated_by) VALUES (:disease_type_id, :disease_code, :disease_name, :description, :status, :created_at, :created_by, :updated_at, :updated_by)")

        db_session.execute(query, data_disease)

        db_session.commit()

        return {"message": "Disease created successfully", "data": data_disease}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def update(disease: DiseaseUpdateRequest, disease_id: int, db_session: Session, token):
    """Update Disease"""
    try:
        # Generate the current datetime
        updated_at = datetime.now()
        updated_by = token.get("id")

        data_disease = {
            "disease_type_id": disease.disease_type_id,
            "disease_code": disease.disease_code,
            "disease_name": disease.disease_name,
            "description": disease.description,
            "status": disease.status,
            "updated_at": updated_at,
            "updated_by": updated_by
        }

        query = text("UPDATE diseases SET disease_type_id = :disease_type_id, disease_code = :disease_code, disease_name = :disease_name, description = :description, status = :status, updated_at = :updated_at, updated_by = :updated_by WHERE disease_id = :disease_id")

        db_session.execute(query, {**data_disease, "disease_id": disease_id})

        db_session.commit()

        return {"message": "Disease updated successfully", "data": data_disease}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def delete(disease_id: int, db_session: Session):
    """Delete Disease"""
    try:
        query = text("DELETE FROM diseases WHERE disease_id = :disease_id")
        db_session.execute(query, {"disease_id": disease_id})
        db_session.commit()

        return {"message": "Disease deleted successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex