from fastapi import APIRouter, Depends, Header, HTTPException, status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from src.config.get_session import get_db_connect
from src.schemas.specialties import SpecialtyRequest, SpecialtyUpdateRequest
from src.services import specialties
from src.utils.security import oauth2_scheme, valid_user, verify_token

router = APIRouter()


@router.get(path="/specialties", status_code=status.HTTP_200_OK, summary="Get All Specialties")
async def get_specialties(
    db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)
):
    """
    ## RESPONSE
        - Returns a list of specialties

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = specialties.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/specialties", status_code=status.HTTP_201_CREATED, summary="Create Specialty")
async def create_specialty(
    specialty: SpecialtyRequest,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## REQUEST BODY
        - specialty_name: str

    ## RESPONSE
        - Returns the created specialty

    ## DEVELOPER NOTES
        - The company_id is a field that is optional

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = specialties.create(specialty, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(
    path="/specialties{specialty_id}", status_code=status.HTTP_200_OK, summary="Update Specialty"
)
async def update_specialty(
    specialty_id: int,
    specialty: SpecialtyUpdateRequest,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## REQUEST BODY
        - specialty_name: str

    ## RESPONSE
        - Returns the updated specialty

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = specialties.update(specialty_id, specialty, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(
    path="/specialties/{specialty_id}", status_code=status.HTTP_200_OK, summary="Delete Specialty"
)
async def delete_specialty(
    specialty_id: int,
    db_session: Session = Depends(get_db_connect),
    token: str = Depends(oauth2_scheme),
):
    """
    ## REQUEST PARAMS
        - specialty_id: int

    ## RESPONSE
        - Returns the deleted specialty

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))

    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = specialties.delete(specialty_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))

    return JSONResponse(content=result, status_code=status.HTTP_200_OK)
