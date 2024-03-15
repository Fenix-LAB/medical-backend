from fastapi import APIRouter
from fastapi import APIRouter, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import diseases_types
from fastapi.responses import JSONResponse
from src.schemas.disease_types import DiseaseTypesRequest, DiseaseTypesUpdateRequest
from src.utils.security import verify_token, valid_user
from src.utils.security import oauth2_scheme

router = APIRouter()

@router.get(path="/disease_types", status_code=status.HTTP_200_OK, summary="Get All Disease Types")
async def get_disease_types(db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)):
    """
    ## RESPONSE
        - Returns a list of disease types

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = diseases_types.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/disease_types", status_code=status.HTTP_201_CREATED, summary="Create Disease Type")
async def create_disease_type(disease_type: DiseaseTypesRequest, db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)):
    """
    ## REQUEST BODY
        - disease_name: str
        - description: str
        - status: int
        - created_by: int
        - updated_by: int

    ## RESPONSE
        - Returns the created disease type
        
    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))
    
    result = diseases_types.create(disease_type, db_session, token)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/disease_types{disease_type_id}", status_code=status.HTTP_200_OK, summary="Update Disease Type")
async def update_disease_type(disease_type: DiseaseTypesUpdateRequest, disease_type_id: int,  db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)):
    """
    ## REQUEST BODY
        - disease_name: str
        - description: str
        - status: int
        - updated_by: int

    ## RESPONSE
        - Returns the updated disease type

    ## DEVELOPER NOTES
        - All fields are optional, but at least one will be required to update the disease type
        
    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))
    
    result = diseases_types.update(disease_type, disease_type_id, db_session, token)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(path="/disease_types{disease_type_id}", status_code=status.HTTP_200_OK, summary="Delete Disease Type")
async def delete_disease_type(disease_type_id: int, db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)):
    """
    ## RESPONSE
        - Returns the deleted disease type
        
    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))
    
    result = diseases_types.delete(disease_type_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)
