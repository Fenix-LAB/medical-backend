from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.schemas.image_exams import ImageExamRequest
from src.utils.ctes import COMPANIES_ROW
from src.utils.helper import clean_dict, rows_to_dicts


def get(db_session: Session):
    """Get All Image Exams"""
    try:
        query = text("SELECT * FROM image_exams")
        image_exams = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        image_exams = rows_to_dicts(image_exams, COMPANIES_ROW)

        return image_exams

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def create(image_exam: ImageExamRequest, db_session: Session, payload):
    """Create Image Exam"""
    try:
        created_at = datetime.now()
        created_by = payload.get("id")

        data_image_exam = {
            "image_type_id": image_exam.image_type_id,
            "company_id": image_exam.company_id,
            "exam_name": image_exam.exam_name,
            "description": image_exam.description,
            "status": 1,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None,
        }

        query = text(
            "INSERT INTO image_exams (image_type_id, company_id, exam_name , description, status, created_at, created_by, updated_at, updated_by) VALUES (:image_type_id, :company_id, :exam_name, :description, :status, :created_at, :created_by, :updated_at, :updated_by)"
        )

        db_session.execute(query, data_image_exam)

        db_session.commit()

        data_image_exam = clean_dict(data_image_exam)

        return {"message": "Image Exam created successfully", "data": data_image_exam}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def update(image_exam_id: int, image_exam: ImageExamRequest, db_session: Session, payload):
    """Update Image Exam"""
    try:
        updated_at = datetime.now()
        updated_by = payload.get("id")

        data_image_exam = {
            "image_type_id": image_exam.image_type_id,
            "company_id": image_exam.company_id,
            "exam_name": image_exam.exam_name,
            "description": image_exam.description,
            "status": 1,
            "updated_at": updated_at,
            "updated_by": updated_by,
        }

        query = text(
            "UPDATE image_exams SET image_type_id = :image_type_id, company_id = :company_id, exam_name = :exam_name, description = :description, status = :status, updated_at = :updated_at, updated_by = :updated_by WHERE image_exam_id = :image_exam_id"
        )

        db_session.execute(query, {**data_image_exam, "image_exam_id": image_exam_id})

        db_session.commit()

        data_image_exam = clean_dict(data_image_exam)

        return {"message": "Image Exam updated successfully", "data": data_image_exam}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def delete(image_exam_id: int, db_session: Session):
    """Delete Image Exam"""
    try:
        query = text("DELETE FROM image_exams WHERE id = :id")
        db_session.execute(query, {"id": image_exam_id})

        db_session.commit()

        return {"message": "Image Exam deleted successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
