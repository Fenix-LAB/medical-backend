from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from src.schemas.insurances import InsurancesRequest, InsurancesUpdateRequest
from src.utils.ctes import INSURANCES_ROW
from src.utils.helper import rows_to_dicts
from datetime import datetime


def get(db_session: Session):
    """Get All Insurances"""
    try:
        query = text("SELECT * FROM insurances")
        insurances = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        insurances = rows_to_dicts(insurances, INSURANCES_ROW)
        
        return insurances

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def create(insurance: InsurancesRequest, db_session: Session, payload):
    """Create Insurance"""
    try:
        created_at = datetime.now()
        created_by = payload.get("id")

        data_insurance = {
            "insurance_name": insurance.insurance_name,
            "person_id": insurance.person_id,
            "policy_number": insurance.policy_number,
            "coverage_details": insurance.coverage_details,
            "status": insurance.status,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None
        }

        query = text("INSERT INTO insurances (insurance_name, person_id, policy_number, coverage_details, status, created_at, created_by, updated_at, updated_by) VALUES (:insurance_name, :person_id, :policy_number, :coverage_details, :status, :created_at, :created_by, :updated_at, :updated_by)")

        db_session.execute(query, data_insurance)

        db_session.commit()

        return {"message": "Insurance created successfully", "data": data_insurance}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def update(insurance_id: int, insurance: InsurancesUpdateRequest, db_session: Session, payload):
    """Update Insurance"""
    try:
        updated_at = datetime.now()
        updated_by = payload.get("id")

        data_insurance = {
            "insurance_name": insurance.insurance_name,
            "person_id": insurance.person_id,
            "policy_number": insurance.policy_number,
            "coverage_details": insurance.coverage_details,
            "status": insurance.status,
            "updated_at": updated_at,
            "updated_by": updated_by
        }

        query = text("UPDATE insurances SET insurance_name = :insurance_name, person_id = :person_id, policy_number = :policy_number, coverage_details = :coverage_details, status = :status, updated_at = :updated_at, updated_by = :updated_by WHERE insurance_id = :insurance_id")

        db_session.execute(query, {**data_insurance, "insurance_id": insurance_id})

        db_session.commit()

        return {"message": "Insurance updated successfully", "data": data_insurance}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def delete(insurance_id: int, db_session: Session):
    """Delete Insurance"""
    try:
        query = text("DELETE FROM insurances WHERE insurance_id = :insurance_id")
        db_session.execute(query, {"insurance_id": insurance_id})
        db_session.commit()

        return {"message": "Insurance deleted successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex