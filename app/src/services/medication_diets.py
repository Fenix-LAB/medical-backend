from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from src.schemas.medication_diets import MedicationDietsRequest, MedicationDietsUpdateRequest
from src.utils.ctes import MEDICATION_DIETS_ROW
from src.utils.helper import rows_to_dicts, clean_dict
from datetime import datetime


def get(db_session: Session):
    """Get All Medication Diets"""
    try:
        query = text("SELECT * FROM medication_diets")
        medication_diets = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        medication_diets = rows_to_dicts(medication_diets, MEDICATION_DIETS_ROW)
        
        return medication_diets

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def create(medication_diet: MedicationDietsRequest, db_session: Session, payload):  
    """Create Medication Diet"""
    try:
        created_at = datetime.now()
        created_by = payload.get("id")

        data_medication_diet = {
            "medication_type_id": medication_diet.medication_type_id,
            "company_id": medication_diet.company_id,
            "medication_diet_name": medication_diet.medication_diet_name,
            "generic_composition": medication_diet.generic_composition,
            "indications": medication_diet.indications,
            "contraindications": medication_diet.contraindications,
            "status": 1,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None
        }

        query = text("INSERT INTO medication_diets (medication_type_id, company_id, medication_diet_name, generic_composition, indications, contraindications, status, created_at, created_by, updated_at, updated_by) VALUES (:medication_type_id, :company_id, :medication_diet_name, :generic_composition, :indications, :contraindications, :status, :created_at, :created_by, :updated_at, :updated_by)")

        db_session.execute(query, data_medication_diet)

        db_session.commit()

        data_medication_diet = clean_dict(data_medication_diet)

        return {"message": "Medication Diet created successfully", "data": data_medication_diet}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def update(medication_diet_id: int, medication_diet: MedicationDietsUpdateRequest, db_session: Session, payload):
    """Update Medication Diet"""
    try:
        updated_at = datetime.now()
        updated_by = payload.get("id")

        data_medication_diet = {
            "medication_type_id": medication_diet.medication_type_id,
            "company_id": medication_diet.company_id,
            "medication_diet_name": medication_diet.medication_diet_name,
            "generic_composition": medication_diet.generic_composition,
            "indications": medication_diet.indications,
            "contraindications": medication_diet.contraindications,
            "status": medication_diet.status,
            "updated_at": updated_at,
            "updated_by": updated_by
        }

        query = text("UPDATE medication_diets SET medication_type_id = :medication_type_id, company_id = :company _id, medication_diet_name = :medication_diet_name, generic_composition = :generic_composition, indications = :indications, contraindications = :contraindications, status = :status, updated_at = :updated_at, updated_by = :updated_by WHERE medication_diet_id = :medication_diet_id")

        db_session.execute(query, {**data_medication_diet, "medication_diet_id": medication_diet_id})

        db_session.commit()

        data_medication_diet = clean_dict(data_medication_diet)

        return {"message": f"Medication Diet with id {medication_diet_id} updated successfully", "data": data_medication_diet}
    
    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def delete(medication_diet_id: int, db_session: Session):
    """Delete Medication Diet"""
    try:
        query = text("DELETE FROM medication_diets WHERE medication_diet_id = :medication_diet_id")
        db_session.execute(query, {"medication_diet_id": medication_diet_id})

        db_session.commit()

        return {"message": "Medication Diet deleted successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex