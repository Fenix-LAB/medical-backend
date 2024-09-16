from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.config.get_session import get_db_connect
from src.schemas.medication_types import (
    MedicationTypesRequest,
    MedicationTypesUpdateRequest,
)
from src.services import medication_types
from src.utils.security import oauth2_scheme, valid_user, verify_token

router = APIRouter()


@router.get(
    path="/medication_types", status_code=status.HTTP_200_OK, summary="Get All Medication Types"
)
async def get_medication_types(
    db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)
):
    """
    ## RESPONSE
        - Returns a list of medication types

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = medication_types.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(
    path="/medication_types", status_code=status.HTTP_201_CREATED, summary="Create Medication Type"
)
async def create_medication_type(
    medication_type: MedicationTypesRequest,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## REQUEST BODY
        - company_id: int
        - medication_name: str
        - description: str

    ## RESPONSE
        - Returns the created medication type

    ## DEVELOPER NOTES
        - The company_id is a field that is required

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = medication_types.create(medication_type, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(
    path="/medication_types/{medication_type_id}",
    status_code=status.HTTP_200_OK,
    summary="Update Medication Type",
)
async def update_medication_type(
    medication_type: MedicationTypesUpdateRequest,
    medication_type_id: int,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## REQUEST BODY
        - company_id: int
        - medication_name: str
        - description: str
        - status: int

    ## RESPONSE
        - Returns the updated medication type

    ## DEVELOPER NOTES
        - The company_id is a field that is required
        - The status is a field that is optional

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = medication_types.update(medication_type_id, medication_type, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(
    path="/medication_types/{medication_type_id}",
    status_code=status.HTTP_200_OK,
    summary="Delete Medication Type",
)
async def delete_medication_type(
    medication_type_id: int,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## RESPONSE
        - Returns the deleted medication type

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = medication_types.delete(medication_type_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)
