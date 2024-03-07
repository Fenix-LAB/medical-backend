from fastapi import APIRouter
from fastapi import APIRouter, Body, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import establishments
from fastapi.responses import JSONResponse
from src.schemas.establishments import EstablishmentRequest, EstablishmentUpdateRequest

router = APIRouter()

@router.get(path="/establishments", status_code=status.HTTP_200_OK, summary="Get All Establishments")
async def get_establishments(db_session: Session = Depends(get_db_connect)):
    """
    ## RESPONSE
        - Returns a list of establishments

    """

    result = establishments.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/establishments", status_code=status.HTTP_201_CREATED, summary="Create Establishment")
async def create_establishment(establishment: EstablishmentRequest, db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST BODY
        - name: str
        - address: str
        - status: bool
        - created_by: int
        - updated_by: int (This field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the created establishment

    """

    result = establishments.create(establishment, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/establishments{establishment_id}", status_code=status.HTTP_200_OK, summary="Update Establishment")
async def update_establishment(establishment: EstablishmentUpdateRequest, establishment_id: int,  db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST BODY
        - name: str (optional)
        - address: str (optional)
        - status: int (optional)
        - updated_by: int (optional, this field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the updated establishment

    """
    result = establishments.update(establishment, establishment_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(path="/establishments{establishment_id}", status_code=status.HTTP_200_OK, summary="Delete Establishment")
async def delete_establishment(establishment_id: int, db_session: Session = Depends(get_db_connect)):
    """
    ## RESPONSE
        - Returns the deleted establishment

    """
    result = establishments.delete(establishment_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)