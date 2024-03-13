from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from src.schemas.companies import CompanyRequest, CompanyUpdateRequest
from src.utils.ctes import COMPANIES_ROW
from src.utils.helper import rows_to_dicts
from datetime import datetime
from src.utils.security import decode_token

def get(db_session: Session):
    """Get All Companies"""
    try:
        query = text("SELECT * FROM companies")
        companies = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        companies = rows_to_dicts(companies, COMPANIES_ROW)
        
        return companies

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def create(company: CompanyRequest, db_session: Session, payload):
    """Create Company"""
    try:
        created_at = datetime.now()
        created_by = payload.get("id")

        data_company = {
            "commercial_name": company.commercial_name,
            "contact_person_id": company.contact_person_id,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None
        }

        query = text("INSERT INTO companies (commercial_name, contact_person_id, created_at, created_by, updated_at, updated_by) VALUES (:commercial_name, :contact_person_id, :created_at, :created_by, :updated_at, :updated_by)")

        db_session.execute(query, data_company)

        db_session.commit()

        return {"message": "Company created successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def update(company_id: int, company: CompanyUpdateRequest, db_session: Session, payload):
    """Update Company"""
    try:
        updated_at = datetime.now()
        updated_by = payload.get("id")

        data_company = {
            "commercial_name": company.commercial_name,
            "contact_person_id": company.contact_person_id,
            "status": company.status,
            "updated_at": updated_at,
            "updated_by": updated_by
        }

        query = text("UPDATE companies SET commercial_name = :commercial_name, contact_person_id = :contact_person_id, status = :status, updated_at = :updated_at, updated_by = :updated_by WHERE company_id = :company_id")

        db_session.execute(query, {**data_company, "company_id": company_id})

        db_session.commit()

        return {"message": f"Company with id {company_id} updated successfully"}
    
    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def delete(company_id: int, db_session: Session):
    """Delete Company"""
    try:
        query = text("DELETE FROM companies WHERE company_id = :company_id")

        db_session.execute(query, {"company_id": company_id})

        db_session.commit()

        return {"message": f"Company with id {company_id} deleted successfully"}
    
    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex