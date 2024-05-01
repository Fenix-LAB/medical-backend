from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.config.get_session import get_db_connect
from src.schemas.doctors import DoctorsRequest, DoctorsUpdateRequest
from src.services import doctors
from src.utils.security import oauth2_scheme, valid_user, verify_token

router = APIRouter()


@router.get(path="/doctors", status_code=status.HTTP_200_OK, summary="Get All Doctors")
async def get_doctors(
    db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)
):
    """
    ## RESPONSE
        - Returns a list of doctors

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = doctors.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/doctors", status_code=status.HTTP_201_CREATED, summary="Create Doctor")
async def create_doctor(
    doctor: DoctorsRequest,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## REQUEST BODY
        - person_id: int (optional)
        - specialty_id: int (optional)
        - license_number: str
        - company_id: int (optional)

    ## RESPONSE
        - Returns the created doctor

    ## DEVELOPER NOTES
        - The person_id and specialty_id are fields that are optional

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = doctors.create(doctor, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/doctors/{doctor_id}", status_code=status.HTTP_200_OK, summary="Update Doctor")
async def update_doctor(
    doctor: DoctorsUpdateRequest,
    doctor_id: int,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## REQUEST BODY
        - person_id: int (optional)
        - specialty_id: int (optional)
        - license_number: str (optional)
        - status: int (optional)
        - company_id: int (optional)

    ## RESPONSE
        - Returns the updated doctor

    ## DEVELOPER NOTES
        - The person_id, specialty_id, license_number, status, and company_id are fields that are optional

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = doctors.update(doctor_id, doctor, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(path="/doctors/{doctor_id}", status_code=status.HTTP_200_OK, summary="Delete Doctor")
async def delete_doctor(
    doctor_id: int,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## RESPONSE
        - Returns a message of success

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = doctors.delete(doctor_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)
