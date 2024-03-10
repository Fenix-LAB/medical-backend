from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import companies
from fastapi.responses import JSONResponse
from src.schemas.companies import CompanyRequest, CompanyUpdateRequest
from src.utils.security import verify_token, valid_user
from src.utils.security import oauth2_scheme

router = APIRouter()

@router.get(path="/companies", status_code=status.HTTP_200_OK, summary="Get All Companies")
async def get_companies(db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)):
    """
    ## RESPONSE
        - Returns a list of companies

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = companies.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/companies", status_code=status.HTTP_201_CREATED, summary="Create Company")
async def create_company(company: CompanyRequest, db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)):
    """
    ## REQUEST BODY
        - commercial_name: str
        - contact_person_id: int (optional)
        - status: bool
        - created_by: int
        - updated_by: int (This field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the created company

    ## DEVELOPER NOTES
        - The contact_person_id is a field that is optional

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = companies.create(company, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/companies{company_id}", status_code=status.HTTP_200_OK, summary="Update Company")
async def update_company(company: CompanyUpdateRequest, company_id: int,  db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)):
    """
    ## REQUEST BODY
        - commercial_name: str (optional)
        - contact_person_id: int (optional)
        - status: int (optional)
        - updated_by: int (optional, this field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the updated company

    ## DEVELOPER NOTES
        - All fields are optional

    """
    
    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))
    
    result = companies.update(company, company_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(path="/companies{company_id}", status_code=status.HTTP_200_OK, summary="Delete Company")
async def delete_company(company_id: int, db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)):
    """
    ## RESPONSE
        - Returns the deleted company

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = companies.delete(company_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)
