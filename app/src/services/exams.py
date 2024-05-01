from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.schemas.exams import ExamsRequest, ExamsUpdateRequest
from src.utils.ctes import EXAMS_ROW
from src.utils.helper import clean_dict, rows_to_dicts


def get(db_session: Session):
    """Get All Exams"""
    try:
        query = text("SELECT * FROM exams")
        exams = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        exams = rows_to_dicts(exams, EXAMS_ROW)

        return exams

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def create(exam: ExamsRequest, db_session: Session, payload):
    """Create Exam"""
    try:
        # Generate the current datetime
        created_at = datetime.now()
        created_by = payload["id"]

        data_exam = {
            "exam_type_id": exam.exam_type_id,
            "company_id": exam.company_id,
            "exam_name": exam.exam_name,
            "description": exam.description,
            "status": 1,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None,
        }

        query = text(
            "INSERT INTO exams (exam_type_id, company_id, exam_name, description, status, created_at, created_by, updated_at, updated_by) VALUES (:exam_type_id, :company_id, :exam_name, :description, :status, :created_at, :created_by, :updated_at, :updated_by)"
        )

        db_session.execute(query, data_exam)

        db_session.commit()

        data_exam = clean_dict(data_exam)

        return {"message": "Exam created successfully", "data": data_exam}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def update(exam: ExamsUpdateRequest, exam_id: int, db_session: Session, payload):
    """Update Exam"""
    try:
        # Generate the current datetime
        updated_at = datetime.now()
        updated_by = payload["id"]

        data_exam = {
            "exam_type_id": exam.exam_type_id,
            "company_id": exam.company_id,
            "exam_name": exam.exam_name,
            "description": exam.description,
            "status": exam.status,
            "updated_at": updated_at,
            "updated_by": updated_by,
        }

        query = text(
            "UPDATE exams SET exam_type_id = :exam_type_id, company_id = :company_id, exam_name = :exam_name, description = :description, status = :status, updated_at = :updated_at, updated_by = :updated_by WHERE exam_id = :exam_id"
        )

        db_session.execute(query, {**data_exam, "exam_id": exam_id})

        db_session.commit()

        data_exam = clean_dict(data_exam)

        return {"message": "Exam updated successfully", "data": data_exam}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def delete(exam_id: int, db_session: Session):
    """Delete Exam"""
    try:
        query = text("DELETE FROM exams WHERE exam_id = :exam_id")

        db_session.execute(query, {"exam_id": exam_id})

        db_session.commit()

        return {"message": "Exam deleted successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
