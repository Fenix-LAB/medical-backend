from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from src.schemas.medical_attentions import MedicalAttentionRequest, MedicalAttentionUpdateRequest
from src.utils.ctes import MEDICAL_ATTENTIONS_ROW
from src.utils.helper import rows_to_dicts, clean_dict
from datetime import datetime


def get(db_session: Session):
    """Get All Medical Attentions"""
    try:
        query = text("SELECT * FROM medical_attentions")
        medical_attentions = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        medical_attentions = rows_to_dicts(medical_attentions, MEDICAL_ATTENTIONS_ROW)
        
        return medical_attentions

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def create(medical_attention: MedicalAttentionRequest, db_session: Session, payload):
    """Create Medical Attention"""
    try:
        created_at = datetime.now()
        created_by = payload.get("id")

        data_medical_attention = {
            "appointment_id": medical_attention.appointment_id,
            "establishment_id": medical_attention.establishment_id,
            "doctor_id": medical_attention.doctor_id,
            "service_id": medical_attention.service_id,
            "insurance_id": medical_attention.insurance_id,
            "company_id": medical_attention.company_id,
            "attention_date": medical_attention.attention_date,
            "symptoms": medical_attention.symptoms,
            "diagnosis": medical_attention.diagnosis,
            "treatment": medical_attention.treatment,
            "current_condition": medical_attention.current_condition,
            "evolution": medical_attention.evolution,
            "next_appointment_date": medical_attention.next_appointment_date,
            "status": 1,
            "created_at": created_at,
            "created_by": created_by,
            "updated_at": None,
            "updated_by": None
        }

        query = text("INSERT INTO medical_attentions (appointment_id, establishment_id, doctor_id, service_id, insurance_id, company_id, attention_date, symptoms, diagnosis, treatment, current_condition, evolution, next_appointment_date, status, created_at, created_by, updated_at, updated_by) VALUES (:appointment_id, :establishment_id, :doctor_id, :service_id, :insurance_id, :company_id, :attention_date, :symptoms, :diagnosis, :treatment, :current_condition, :evolution, :next_appointment_date, :status, :created_at, :created_by, :updated_at, :updated_by)")

        db_session.execute(query, data_medical_attention)

        db_session.commit()

        data_medical_attention = clean_dict(data_medical_attention)

        return {"message": "Medical Attention created successfully", "data": data_medical_attention}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def update(medical_attention_id: int, medical_attention: MedicalAttentionUpdateRequest, db_session: Session, payload):
    """Update Medical Attention"""
    try:
        updated_at = datetime.now()
        updated_by = payload.get("id")

        data_medical_attention = {
            "appointment_id": medical_attention.appointment_id,
            "establishment_id": medical_attention.establishment_id,
            "doctor_id": medical_attention.doctor_id,
            "service_id": medical_attention.service_id,
            "insurance_id": medical_attention.insurance_id,
            "company_id": medical_attention.company_id,
            "attention_date": medical_attention.attention_date,
            "symptoms": medical_attention.symptoms,
            "diagnosis": medical_attention.diagnosis,
            "treatment": medical_attention.treatment,
            "current_condition": medical_attention.current_condition,
            "evolution": medical_attention.evolution,
            "next_appointment_date": medical_attention.next_appointment_date,
            "status": medical_attention.status,
            "updated_at": updated_at,
            "updated_by": updated_by
        }

        query = text("UPDATE medical_attentions SET appointment_id = :appointment_id, establishment_id = :establishment_id, doctor_id = :doctor_id, service_id = :service_id, insurance_id = :insurance_id, company_id = :company_id, attention_date = :attention_date, symptoms = :symptoms, diagnosis = :diagnosis, treatment = :treatment, current_condition = :current_condition, evolution = :evolution, next_appointment_date = :next_appointment_date, status = :status, updated_at = :updated_at, updated_by = :updated_by WHERE attention_id = :attention_id")

        db_session.execute(query, {**data_medical_attention, "attention_id": medical_attention_id})

        db_session.commit()

        data_medical_attention = clean_dict(data_medical_attention)

        return {"message": f"Medical Attention with id {medical_attention_id} updated successfully", "data": data_medical_attention}
    
    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def delete(medical_attention_id: int, db_session: Session):
    """Delete Medical Attention"""
    try:
        query = text("DELETE FROM medical_attentions WHERE attention_id = :attention_id")
        db_session.execute(query, {"attention_id": medical_attention_id})

        db_session.commit()

        return {"message": f"Medical Attention with id {medical_attention_id} deleted successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex