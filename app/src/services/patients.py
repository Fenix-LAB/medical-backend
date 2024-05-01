from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from src.schemas.patients import PatientRequest, PatientUpdateRequest
from src.utils.ctes import PATIENTS_ROW, PERSONS_ROW
from src.utils.helper import rows_to_dicts
from datetime import datetime


def get(db_session: Session):
    """Get All Patients"""
    try:
        query = text("SELECT * FROM patients")
        patients = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        patients = rows_to_dicts(patients, PATIENTS_ROW)

        for patient in patients:
            patient["income_date"] = patient["income_date"].strftime("%Y-%m-%d")

            person_id = patient.get("person_id")

            # Get person details
            query = text("SELECT * FROM persons WHERE person_id = :person_id")
            person = db_session.execute(query, {"person_id": person_id}).fetchone()

            if person:
                person = rows_to_dicts([person], PERSONS_ROW)[0]
                person["birthdate"] = person["birthdate"].strftime("%Y-%m-%d")
                patient["person"] = person

        return patients

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def create(patient: PatientRequest, db_session: Session, payload):
    """Create Patient"""
    try:
        created_at = datetime.now()
        created_by = payload.get("id")

        data_patient = {
            "person_id": patient.person_id,
            "category": patient.category,
            "occupation_ref": patient.occupation_ref,
            "income_date": patient.income_date,
            "is_client": patient.is_client,
            "insurance": patient.insurance,
            "alert_1": patient.alert_1,
            "alert_2": patient.alert_2,
            "alert_3": patient.alert_3,
            "company_id": patient.company_id,
            "status": 1,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None,
        }

        query = text(
            """
            INSERT INTO patients (
                person_id, category, occupation_ref, income_date, is_client, 
                insurance, alert_1, alert_2, alert_3, company_id, status, 
                created_at, created_by, updated_at, updated_by
            ) VALUES (
                :person_id, :category, :occupation_ref, :income_date, :is_client, 
                :insurance, :alert_1, :alert_2, :alert_3, :company_id, :status, 
                :created_at, :created_by, :updated_at, :updated_by
            ) RETURNING patient_id
        """
        )

        result = db_session.execute(query, data_patient)
        patient_id = result.fetchone()[0]

        data_patient["created_at"] = data_patient["created_at"].strftime("%Y-%m-%d")
        data_patient["income_date"] = data_patient["income_date"].strftime("%Y-%m-%d")

        db_session.commit()

        data_patient["patient_id"] = patient_id

        return {"message": "Patient created successfully", "data": data_patient}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def update(
    patient_id: int, patient: PatientUpdateRequest, db_session: Session, payload
):
    """Update Patient"""
    try:
        updated_at = datetime.now()
        updated_by = payload.get("id")

        data_patient = {
            "person_id": patient.person_id,
            "category": patient.category,
            "occupation_ref": patient.occupation_ref,
            "income_date": patient.income_date,
            "is_client": patient.is_client,
            "insurance": patient.insurance,
            "alert_1": patient.alert_1,
            "alert_2": patient.alert_2,
            "alert_3": patient.alert_3,
            "company_id": patient.company_id,
            "status": patient.status,
            "updated_at": updated_at,
            "updated_by": updated_by,
        }

        query = text(
            "UPDATE patients SET person_id = :person_id, category = :category, occupation_ref = :occupation_ref, income_date = :income_date, is_client = :is_client, insurance = :insurance, alert_1 = :alert_1, alert_2 = :alert_2, alert_3 = :alert_3, company_id = :company_id, status = :status, updated_at = :updated_at, updated_by = :updated_by WHERE patient_id = :patient_id"
        )

        db_session.execute(query, {**data_patient, "patient_id": patient_id})

        # data_patient["created_at"] = data_patient["created_at"].strftime("%Y-%m-%d")
        data_patient["updated_at"] = data_patient["updated_at"].strftime("%Y-%m-%d")
        data_patient["income_date"] = data_patient["income_date"].strftime("%Y-%m-%d")

        db_session.commit()

        return {
            "message": f"Patient with id {patient_id} updated successfully",
            "data": data_patient,
        }

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex


def delete(patient_id: int, db_session: Session):
    """Delete Patient"""
    try:
        query = text("DELETE FROM patients WHERE patient_id = :patient_id")
        db_session.execute(query, {"patient_id": patient_id})

        db_session.commit()

        return {"message": f"Patient with id {patient_id} deleted successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
