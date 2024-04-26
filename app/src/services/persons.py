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

        # Convert birthdate to string
        for person in persons:
            person["birthdate"] = person["birthdate"].strftime("%Y-%m-%d")
        
        return persons

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def create(person: PersonsRequest, db_session: Session, payload):    
    """Create Person"""
    try:

        created_at = date.today()
        created_by = payload.get("id")

        # Construye la consulta SQL con SQLAlchemy para evitar SQL injection
        query = text("""
            INSERT INTO persons (
                first_name, last_name, identification_type, identification, 
                birthdate, gender, marital_status, address, phone_number, 
                email, created_at, created_by, updated_at, updated_by, company_id
            ) VALUES (
                :first_name, :last_name, :identification_type, :identification, 
                :birthdate, :gender, :marital_status, :address, :phone_number, 
                :email, :created_at, :created_by, :updated_at, :updated_by, :company_id
            ) RETURNING person_id
        """)

        # Ejecuta la consulta SQL con los datos del objeto person y recupera el ID generado
        result = db_session.execute(query, {
            "first_name": person.first_name,
            "last_name": person.last_name,
            "identification_type": person.identification_type,
            "identification": person.identification,
            "birthdate": person.birthdate,
            "gender": person.gender,
            "marital_status": person.marital_status,
            "address": person.address,
            "phone_number": person.phone_number,
            "email": person.email,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None,
            "company_id": person.company_id
        })

        # Recupera el ID insertado desde el resultado de la consulta
        last_inserted_id = result.fetchone()[0]

        # Actualiza el objeto person con el ID insertado
        person.person_id = last_inserted_id

        # Convierte las fechas a formato de cadena
        person.birthdate = person.birthdate.strftime("%Y-%m-%d")
        created_at = created_at.strftime("%Y-%m-%d")

        # Confirma los cambios en la base de datos
        db_session.commit()

        # Retorna la respuesta con los datos de la persona
        return {
            "message": "Person created successfully",
            "data": person.dict()
        }
    
    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def update(person: PersonsUpdateRequest, person_id: int, db_session: Session, payload):
    """Update Person"""
    try:
        update_at = date.today()
        updated_by = payload.get("id")
        
        data_person = {
            "first_name": person.first_name,
            "last_name": person.last_name,
            "identification_type": person.identification_type,
            "identification": person.identification,
            "birthdate": person.birthdate,
            "gender": person.gender,
            "marital_status": person.marital_status,
            "address": person.address,
            "phone_number": person.phone_number,
            "email": person.email,
            "updated_at": update_at,
            "updated_by": updated_by,
            "company_id": person.company_id
        }

        query = text("UPDATE persons SET first_name = :first_name, last_name = :last_name, identification_type = :identification_type, identification = :identification, birthdate = :birthdate, gender = :gender, marital_status = :marital_status, address = :address, phone_number = :phone_number, email = :email, updated_at = :updated_at, updated_by = :updated_by, company_id = :company_id WHERE person_id = :person_id")

        db_session.execute(query, {**data_person, "person_id": person_id})

        db_session.commit()

        data_person["created_at"] = data_person["created_at"].strftime("%Y-%m-%d")
        data_person["updated_at"] = data_person["updated_at"].strftime("%Y-%m-%d")

        return {"message": "Person updated successfully", "data": data_person}
    
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