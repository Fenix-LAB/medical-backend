from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from src.schemas.image_type import ImageTypeRequest, ImageTypeUpdateRequest
from src.utils.ctes import IMAGE_TYPES_ROW
from src.utils.helper import rows_to_dicts, clean_dict
from datetime import datetime


def get(db_session: Session):
    """Get All Image Types"""
    try:
        query = text("SELECT * FROM image_types")
        image_types = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        image_types = rows_to_dicts(image_types, IMAGE_TYPES_ROW)
        
        return image_types

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def create(image_type: ImageTypeRequest, db_session: Session, payload):
    """Create Image Type"""
    try:
        # Generate the current datetime
        created_at = datetime.now()
        created_by = payload["id"]

        data_image_type = {
            "company_id": image_type.company_id,
            "image_type_name": image_type.image_type_name,
            "description": image_type.description,
            "status": 1,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None
        }

        query = text("INSERT INTO image_types (company_id, image_type_name, description, status, created_at, created_by, updated_at, updated_by) VALUES (:company_id, :image_type_name, :description, :status, :created_at, :created_by, :updated_at, :updated_by)")

        db_session.execute(query, data_image_type)

        db_session.commit()

        data_image_type = clean_dict(data_image_type)

        return {"message": "Image Type created successfully", "data": data_image_type}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def update(image_type_id: int, image_type: ImageTypeUpdateRequest, db_session: Session, payload):
    """Update Image Type"""
    try:
        updated_at = datetime.now()
        updated_by = payload.get("id")

        data_image_type = {
            "image_type_name": image_type.image_type_name,
            "description": image_type.description,
            "status": image_type.status,
            "updated_at": updated_at,
            "updated_by": updated_by
        }

        query = text("UPDATE image_types SET image_type_name = :image_type_name, description = :description, status = :status, updated_at = :updated_at, updated_by = :updated_by WHERE id = :id")

        db_session.execute(query, {**data_image_type, "id": image_type_id})

        db_session.commit()

        data_image_type = clean_dict(data_image_type)

        return {"message": "Image Type updated successfully", "data": data_image_type}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def delete(image_type_id: int, db_session: Session):
    """Delete Image Type"""
    try:
        query = text("DELETE FROM image_types WHERE id = :id")
        db_session.execute(query, {"id": image_type_id})
        db_session.commit()

        return {"message": "Image Type deleted successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex

                     