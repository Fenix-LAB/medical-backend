from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.schemas.establishments import EstablishmentRequest, EstablishmentUpdateRequest
from src.utils.ctes import ESTABLISHMENTS_ROW
from src.utils.helper import clean_dict, rows_to_dicts


def get(db_session: Session):
    """Get All Establishments"""
    try:
        query = text("SELECT * FROM establishments")
        establishments = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        establishments = rows_to_dicts(establishments, ESTABLISHMENTS_ROW)

        return establishments

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def create(establishment: EstablishmentRequest, db_session: Session, payload):
    try:
        # Generate the current datetime
        created_at = datetime.now()
        created_by = payload["id"]

        data_establishment = {
            "company_id": establishment.company_id,
            "establishment_name": establishment.establishment_name,
            "establishment_number": establishment.establishment_number,
            "address": establishment.address,
            "city": establishment.city,
            "country": establishment.country,
            "status": 1,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None,
        }

        query = text(
            "INSERT INTO establishments (company_id, establishment_name, establishment_number, address, city, country, status, created_at, created_by, updated_at, updated_by) VALUES (:company_id, :establishment_name, :establishment_number, :address, :city, :country, :status, :created_at, :created_by, :updated_at, :updated_by)"
        )

        db_session.execute(query, data_establishment)

        db_session.commit()

        data_establishment = clean_dict(data_establishment)

        return {"message": "Establishment created successfully", "data": data_establishment}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def update(
    establishment: EstablishmentUpdateRequest, establishment_id: int, db_session: Session, payload
):
    """Update Establishment"""
    try:
        # Generate the current datetime
        updated_at = datetime.now()
        updated_by = payload["id"]

        data_establishment = {
            "establishment_name": establishment.establishment_name,
            "establishment_number": establishment.establishment_number,
            "address": establishment.address,
            "city": establishment.city,
            "country": establishment.country,
            "status": establishment.status,
            "updated_at": updated_at,
            "updated_by": updated_by,
        }

        query = text(
            "UPDATE establishments SET establishment_name = :establishment_name, establishment_number = :establishment_number, address = :address, city = :city, country = :country, status = :status, updated_at = :updated_at, updated_by = :updated_by WHERE establishment_id = :establishment_id"
        )

        db_session.execute(query, {**data_establishment, "establishment_id": establishment_id})

        db_session.commit()

        data_establishment = clean_dict(data_establishment)

        return {"message": "Establishment updated successfully", "data": data_establishment}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def delete(establishment_id: int, db_session: Session):
    """Delete Establishment"""
    try:
        query = text("DELETE FROM establishments WHERE establishment_id = :establishment_id")
        db_session.execute(query, {"establishment_id": establishment_id})

        db_session.commit()

        return {"message": "Establishment deleted successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
