from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.config.get_session import get_db_connect
from src.schemas.medical_attentions import (
    MedicalAttentionRequest,
    MedicalAttentionUpdateRequest,
)
from src.services import medical_attentions
from src.utils.security import oauth2_scheme, valid_user, verify_token

router = APIRouter()


@router.get(
    path="/medical-attentions", status_code=status.HTTP_200_OK, summary="Get All Medical Attentions"
)
async def get_medical_attentions(
    db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)
):
    """
    ## RESPONSE
        - Returns a list of medical attentions

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = medical_attentions.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(
    path="/medical-attentions",
    status_code=status.HTTP_201_CREATED,
    summary="Create Medical Attention",
)
async def create_medical_attention(
    medical_attention: MedicalAttentionRequest,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## REQUEST BODY
        - appointment_id: int (optional)
        - establishment_id: int (optional)
        - doctor_id: int (optional)
        - service_id: int (optional)
        - insurance_id: int (optional)
        - company_id: int (optional)
        - attention_date: date
        - symptoms: str
        - diagnosis: str
        - treatment: str
        - current_condition: str
        - evolution: str
        - next_appointment_date: date

    ## RESPONSE
        - Returns the created medical attention

    ## DEVELOPER NOTES
        - The appointment_id, establishment_id, doctor_id, service_id, insurance_id, and company_id are fields that are optional

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = medical_attentions.create(medical_attention, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(
    path="/medical-attentions/{attention_id}",
    status_code=status.HTTP_200_OK,
    summary="Update Medical Attention",
)
async def update_medical_attention(
    medical_attention: MedicalAttentionUpdateRequest,
    attention_id: int,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## REQUEST BODY
        - appointment_id: int (optional)
        - establishment_id: int (optional)
        - doctor_id: int (optional)
        - service_id: int (optional)
        - insurance_id: int (optional)
        - company_id: int (optional)
        - attention_date: date (optional)
        - symptoms: str (optional)
        - diagnosis: str (optional)
        - treatment: str (optional)
        - current_condition: str (optional)
        - evolution: str (optional)
        - next_appointment_date: date (optional)
        - status: int (optional)

    ## RESPONSE
        - Returns the updated medical attention

    ## DEVELOPER NOTES
        - All fields are optional
    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = medical_attentions.update(medical_attention, attention_id, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(
    path="/medical-attentions/{attention_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete Medical Attention",
)
async def delete_medical_attention(
    attention_id: int,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## RESPONSE
        - Returns the deleted medical attention

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = medical_attentions.delete(attention_id, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)
