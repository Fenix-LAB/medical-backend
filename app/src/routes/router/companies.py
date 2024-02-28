from fastapi import APIRouter
from fastapi import APIRouter, Body, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import companies
from fastapi.responses import JSONResponse
from src.schemas.companies import CompanyRequest, CompanyUpdateRequest

router = APIRouter()

@router.get(path="/companies", status_code=status.HTTP_200_OK, summary="Get All Companies")
async def get_companies(db_session: Session = Depends(get_db_connect)):
    """
    ## RESPONSE
        - Returns a list of companies

    """

    result = companies.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/companies", status_code=status.HTTP_201_CREATED, summary="Create Company")
async def create_company(company: CompanyRequest, db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST BODY
        - commercial_name: str
        - contact_person_id: int (optional)
        - status: bool
        - created_at: date
        - created_by: int
        - updated_at: date
        - updated_by: int

    ## RESPONSE
        - Returns the created company

    ## DEVELOPER NOTES
        - The contact_person_id is a field that is optional

    """

    result = companies.create(company, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/companies{company_id}", status_code=status.HTTP_200_OK, summary="Update Company")
async def update_company(company: CompanyUpdateRequest, company_id: int,  db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST BODY
        - commercial_name: str
        - contact_person_id: int (optional)
        - status: int
        - created_at: date
        - created_by: int
        - updated_at: date
        - updated_by: int

    ## RESPONSE
        - Returns the updated company

    ## DEVELOPER NOTES
        - The contact_person_id is a field that is optional

    """
    print(f'company: {company}')
    result = companies.update(company, company_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(path="/companies{company_id}", status_code=status.HTTP_200_OK, summary="Delete Company")
async def delete_company(company_id: int, db_session: Session = Depends(get_db_connect)):
    """
    ## RESPONSE
        - Returns the deleted company

    """

    result = companies.delete(company_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)
