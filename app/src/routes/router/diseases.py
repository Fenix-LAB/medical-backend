from fastapi import APIRouter
from fastapi import APIRouter, Body, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import diseases
from fastapi.responses import JSONResponse
from src.schemas.diseases import DiseaseRequest, DiseaseUpdateRequest
from src.utils.security import verify_token, valid_user

router = APIRouter()

@router.get(path="/diseases", status_code=status.HTTP_200_OK, summary="Get All Diseases")
async def get_diseases(db_session: Session = Depends(get_db_connect), token: str = Header(..., alias="x-token")):
    """
    ## RESPONSE
        - Returns a list of diseases

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = diseases.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/diseases", status_code=status.HTTP_201_CREATED, summary="Create Disease")
async def create_disease(disease: DiseaseRequest, db_session: Session = Depends(get_db_connect), token: str = Header(..., alias="x-token")):
    """
    ## REQUEST BODY
        - disease_type_id: int (optional)
        - disease_code: str
        - disease_name: str
        - description: str (optional)
        - status: int
        - created_by: int
        - updated_by: int (This field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the created disease

    ## DEVELOPER NOTES
        - The disease_type_id and description are fields that are optional

    """

    result = diseases.create(disease, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/diseases{disease_id}", status_code=status.HTTP_200_OK, summary="Update Disease")
async def update_disease(disease: DiseaseUpdateRequest, disease_id: int,  db_session: Session = Depends(get_db_connect), token: str = Header(..., alias="x-token")):
    """
    ## REQUEST BODY
        - disease_type_id: int (optional)
        - disease_code: str (optional)
        - disease_name: str (optional)
        - description: str (optional)
        - status: int (optional)
        - updated_by: int (optional, this field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the updated disease

    ## DEVELOPER NOTES
        - The disease_type_id, disease_code, disease_name, description and status are fields that are optional

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = diseases.update(disease, disease_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(path="/diseases{disease_id}", status_code=status.HTTP_200_OK, summary="Delete Disease")
async def delete_disease(disease_id: int, db_session: Session = Depends(get_db_connect), token: str = Header(..., alias="x-token")):
    """
    ## RESPONSE
        - Returns a message that indicates that the disease was deleted successfully

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = diseases.delete(disease_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)