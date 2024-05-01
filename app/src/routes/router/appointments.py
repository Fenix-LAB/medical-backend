from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.config.get_session import get_db_connect
from src.schemas.appointments import AppointmentRequest, AppointmentUpdateRequest
from src.services import appointments
from src.utils.security import oauth2_scheme, valid_user, verify_token

router = APIRouter()


@router.get(path="/appointments", status_code=status.HTTP_200_OK, summary="Get All Appointments")
async def get_appointments(
    db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)
):
    """
    ## RESPONSE
        - Returns a list of appointments

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = appointments.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(
    path="/appointments", status_code=status.HTTP_201_CREATED, summary="Create Appointment"
)
async def create_appointment(
    appointment: AppointmentRequest,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## REQUEST BODY
        - patient_id: int
        - doctor_id: int
        - insurance_id: int
        - establishment_id: int
        - appointment_date: date
        - duration_minutes: int
        - notes: str (optional)

    ## RESPONSE
        - Returns the created appointment

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = appointments.create(appointment, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(
    path="/appointments/{appointment_id}",
    status_code=status.HTTP_200_OK,
    summary="Update Appointment",
)
async def update_appointment(
    appointment: AppointmentUpdateRequest,
    appointment_id: int,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## REQUEST BODY
        - patient_id: int (optional)
        - doctor_id: int (optional)
        - insurance_id: int (optional)
        - establishment_id: int (optional)
        - appointment_date: date (optional)
        - duration_minutes: int (optional)
        - status: int (optional)
        - notes: str (optional)

    ## RESPONSE
        - Returns the updated appointment

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = appointments.update(appointment, appointment_id, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(
    path="/appointments/{appointment_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete Appointment",
)
async def delete_appointment(
    appointment_id: int,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## RESPONSE
        - Returns the deleted appointment

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = appointments.delete(appointment_id, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)
