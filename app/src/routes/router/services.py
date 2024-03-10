from fastapi import APIRouter
from fastapi import APIRouter, Body, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import services
from fastapi.responses import JSONResponse
from src.schemas.services import ServiceRequest, ServiceUpdateRequest
from src.utils.security import verify_token, valid_user

router = APIRouter()

@router.get(path="/services", status_code=status.HTTP_200_OK, summary="Get All Services")
async def get_services(db_session: Session = Depends(get_db_connect), token: str = Header(..., alias="x-token")):
    """
    ## RESPONSE
        - Returns a list of services

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = services.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/services", status_code=status.HTTP_201_CREATED, summary="Create Service")
async def create_service(service: ServiceRequest, db_session: Session = Depends(get_db_connect), token: str = Header(..., alias="x-token")):
    """
    ## REQUEST BODY
        - service_name: str
        - description: str (optional)
        - price: float
        - iva_percentage: float
        - status: int
        - created_by: int
        - updated_by: int (This field will be added automatically by the system, so it is not necessary to send it in the request body)
        - company_id: int (optional)
        - specialty_id: int (optional)

    ## RESPONSE
        - Returns the created service

    ## DEVELOPER NOTES
        - The description, company_id and specialty_id are fields that are optional

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = services.create(service, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/services{service_id}", status_code=status.HTTP_200_OK, summary="Update Service")
async def update_service(service: ServiceUpdateRequest, service_id: int,  db_session: Session = Depends(get_db_connect), token: str = Header(..., alias="x-token")):
    """
    ## REQUEST BODY
        - service_name: str (optional)
        - description: str (optional)
        - price: float (optional)
        - iva_percentage: float (optional)
        - status: int (optional)
        - updated_by: int (optional, this field will be added automatically by the system, so it is not necessary to send it in the request body)
        - company_id: int (optional)
        - specialty_id: int (optional)

    ## RESPONSE
        - Returns the updated service

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = services.update(service, service_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(path="/services{service_id}", status_code=status.HTTP_200_OK, summary="Delete Service")
async def delete_service(service_id: int, db_session: Session = Depends(get_db_connect), token: str = Header(..., alias="x-token")):
    """
    ## RESPONSE
        - Returns a message that indicates that the service was deleted successfully

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = services.delete(service_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)