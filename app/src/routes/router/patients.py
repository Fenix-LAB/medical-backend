from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.config.get_session import get_db_connect
from src.schemas.patients import PatientRequest, PatientUpdateRequest
from src.services import patients
from src.utils.security import oauth2_scheme, valid_user, verify_token

router = APIRouter()


@router.get(path="/patients", status_code=status.HTTP_200_OK, summary="Get All Patients")
async def get_patients(
    db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)
):
    """
    ## RESPONSE
        - Returns a list of patients

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = patients.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/patients", status_code=status.HTTP_201_CREATED, summary="Create Patient")
async def create_patient(
    patient: PatientRequest,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## REQUEST BODY
        - category: str
        - occupation_ref: str
        - income_date: date
        - is_client: bool
        - insurance: str
        - alert_1: str
        - alert_2: str
        - alert_3: str

    ## RESPONSE
        - Returns the created patient

    ## DEVELOPER NOTES
        - The contact_person_id is a field that is optional

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = patients.create(patient, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/patients/{patient_id}", status_code=status.HTTP_200_OK, summary="Update Patient")
async def update_patient(
    patient: PatientUpdateRequest,
    patient_id: int,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## REQUEST BODY
        - category: str (optional)
        - occupation_ref: str (optional)
        - income_date: date (optional)
        - is_client: bool (optional)
        - insurance: str (optional)
        - alert_1: str (optional)
        - alert_2: str (optional)
        - alert_3: str (optional)
        - status: int (optional)

    ## RESPONSE
        - Returns the updated patient

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = patients.update(patient_id, patient, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(
    path="/patients/{patient_id}", status_code=status.HTTP_200_OK, summary="Delete Patient"
)
async def delete_patient(
    patient_id: int,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## RESPONSE
        - Returns the deleted patient

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = patients.delete(patient_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)
