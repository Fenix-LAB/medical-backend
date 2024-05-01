from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from src.schemas.services import ServiceRequest, ServiceUpdateRequest
from src.utils.ctes import SERVICE_ROW
from src.utils.helper import clean_dict, rows_to_dicts


def get(db_session: Session):
    """Get All Services"""
    try:
        query = text("SELECT * FROM services")
        services = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        services = rows_to_dicts(services, SERVICE_ROW)

        return services

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def create(service: ServiceRequest, db_session: Session, payload):
    """Create Service"""
    try:
        # Generate the current datetime
        created_at = datetime.now()
        created_by = payload.get("id")

        data_service = {
            "service_name": service.service_name,
            "description": service.description,
            "price": service.price,
            "iva_percentage": service.iva_percentage,
            "status": 1,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None,
            "company_id": service.company_id,
            "specialty_id": service.specialty_id,
        }

        query = text(
            "INSERT INTO services (service_name, description, price, iva_percentage, status, created_at, created_by, updated_at, updated_by, company_id, specialty_id) VALUES (:service_name, :description, :price, :iva_percentage, :status, :created_at, :created_by, :updated_at, :updated_by, :company_id, :specialty_id)"
        )

        db_session.execute(query, data_service)

        db_session.commit()

        data_service = clean_dict(data_service)

        return {"message": "Service created successfully", "data": data_service}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def update(service: ServiceUpdateRequest, service_id: int, db_session: Session, payload):
    """Update Service"""
    try:
        # Generate the current datetime
        updated_at = datetime.now()
        updated_by = payload.get("id")

        data_service = {
            "service_name": service.service_name,
            "description": service.description,
            "price": service.price,
            "iva_percentage": service.iva_percentage,
            "status": service.status,
            "updated_at": updated_at,
            "updated_by": updated_by,
            "company_id": service.company_id,
            "specialty_id": service.specialty_id,
        }

        query = text(
            "UPDATE services SET service_name = :service_name, description = :description, price = :price, iva_percentage = :iva_percentage, status = :status, updated_at = :updated_at, updated_by = :updated_by, company_id = :company_id, specialty_id = :specialty_id WHERE service_id = :service_id"
        )

        db_session.execute(query, {**data_service, "service_id": service_id})

        db_session.commit()

        data_service = clean_dict(data_service)

        return {"message": "Service updated successfully", "data": data_service}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def delete(service_id: int, db_session: Session):
    """Delete Service"""
    try:
        query = text("DELETE FROM services WHERE service_id = :service_id")

        db_session.execute(query, {"service_id": service_id})

        db_session.commit()

        return {"message": "Service deleted successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
