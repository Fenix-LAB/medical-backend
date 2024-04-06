from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from src.schemas.exam_types import ExamTypesRequest, ExamTypesUpdateRequest
from src.utils.ctes import EXAM_TYPES_ROW
from src.utils.helper import rows_to_dicts
from datetime import datetime


def get(db_session: Session):
    """Get All Exam Types"""
    try:
        query = text("SELECT * FROM exam_types")
        exam_types = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        exam_types = rows_to_dicts(exam_types, EXAM_TYPES_ROW)
        
        return exam_types

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    


def create(exam_type: ExamTypesRequest, db_session: Session, payload):
    """Create Exam Type"""
    try:
        # Generate the current datetime
        created_at = datetime.now()
        created_by = payload["id"]

        data_exam_type = {
            "company_id": exam_type.company_id,
            "exam_name": exam_type.exam_name,
            "description": exam_type.description,
            "status": 1,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None
        }

        query = text("INSERT INTO exam_types (company_id, exam_name, description, status, created_at, created_by, updated_at, updated_by) VALUES (:company_id, :exam_name, :description, :status, :created_at, :created_by, :updated_at, :updated_by)")

        db_session.execute(query, data_exam_type)

        db_session.commit()

        return {"message": "Exam Type created successfully", "data": data_exam_type}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def update(exam_type: ExamTypesUpdateRequest, exam_type_id: int, db_session: Session, payload):
    """Update Exam Type"""
    try:
        # Generate the current datetime
        updated_at = datetime.now()
        updated_by = payload["id"]

        data_exam_type = {
            "company_id": exam_type.company_id,
            "exam_name": exam_type.exam_name,
            "description": exam_type.description,
            "status": exam_type.status,
            "updated_at": updated_at,
            "updated_by": updated_by
        }

        query = text("UPDATE exam_types SET company_id = :company_id, exam_name = :exam_name, description = :description, status = :status, updated_at = :updated_at, updated_by = :updated_by WHERE exam_type_id = :exam_type_id")

        db_session.execute(query, {**data_exam_type, "exam_type_id": exam_type_id})

        db_session.commit()

        return {"message": "Exam Type updated successfully", "data": data_exam_type}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def delete(exam_type_id: int, db_session: Session):
    """Delete Exam Type"""
    try:
        query = text("DELETE FROM exam_types WHERE exam_type_id = :exam_type_id")
        db_session.execute(query, {"exam_type_id": exam_type_id})
        db_session.commit()

        return {"message": "Exam Type deleted successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex