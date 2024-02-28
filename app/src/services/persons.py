from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from src.schemas.persons import PersonsRequest, PersonsUpdateRequest
from src.utils.ctes import PERSONS_ROW
from src.utils.helper import rows_to_dicts
from datetime import date

def get(db_session: Session):
    """Get All Persons"""
    try:
        query = text("SELECT * FROM persons")
        persons = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        persons = rows_to_dicts(persons, PERSONS_ROW)
        
        return persons

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def create(person: PersonsRequest, db_session: Session):    
    """Create Person"""
    try:

        created_at = date.today()
        updated_at = date.today()

        person = person.dict()
        person["created_at"] = created_at
        person["updated_at"] = updated_at

        query = text("INSERT INTO persons (first_name, last_name, identification_type, identification, birthdate, gender, marital_status, address, phone_number, email, created_at, created_by, updated_at, updated_by, company_id) VALUES (:first_name, :last_name, :identification_type, :identification, :birthdate, gender, marital_status, address, phone_number, email, created_at, created_by, updated_at, updated_by, company_id)")

        db_session.execute(query, person.dict())

        db_session.commit()

        return {"message": "Person created successfully"}
    
    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def update(person: PersonsUpdateRequest, person_id: int, db_session: Session):
    """Update Person"""
    try:
        update_at = date.today()
        person = person.dict()
        person["updated_at"] = update_at

        query = text("UPDATE persons SET first_name = :first_name, last_name = :last_name, identification_type = :identification_type, identification = :identification, birthdate = :birthdate, gender = :gender, marital_status = :marital_status, address = :address, phone_number = :phone_number, email = :email, updated_at = :updated_at, updated_by = :updated_by, company_id = :company_id WHERE person_id = :person_id")

        db_session.execute(query, {**person, "person_id": person_id})

        db_session.commit()

        return {"message": "Person updated successfully"}
    
    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def delete(person_id: int, db_session: Session):
    """Delete Person"""
    try:
        query = text("DELETE FROM persons WHERE person_id = :person_id")
        db_session.execute(query, {"person_id": person_id})

        db_session.commit()

        return {"message": "Person deleted successfully"}
    
    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex