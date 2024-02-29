from fastapi import APIRouter
from fastapi import APIRouter, Body, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import persons
from fastapi.responses import JSONResponse
from src.schemas.persons import PersonsRequest, PersonsUpdateRequest

router = APIRouter()

@router.get(path="/persons", status_code=status.HTTP_200_OK, summary="Get All Persons")
async def get_persons(db_session: Session = Depends(get_db_connect)):
    """
    ## RESPONSE
        - Returns a list of persons

    """

    result = persons.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/persons", status_code=status.HTTP_201_CREATED, summary="Create Person")
async def create_person(person: PersonsRequest, db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST BODY
        - person_id: int
        - first_name: str
        - last_name: str
        - identification_type: int
        - identification: str
        - birthdate: date
        - gender: str
        - marital_status: str
        - address: str
        - phone_number: str
        - email: str
        - created_by: int (This field will be added automatically by the system, so it is not necessary to send it in the request body)
        - updated_by: int (This field will be added automatically by the system, so it is not necessary to send it in the request body)
        - company_id: int

    ## RESPONSE
        - Returns the created person
        
    """
    
    result = persons.create(person, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/persons{person_id}", status_code=status.HTTP_200_OK, summary="Update Person")
async def update_person(person: PersonsUpdateRequest, person_id: int,  db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST BODY
        - first_name: str
        - last_name: str
        - identification_type: int
        - identification: str
        - birthdate: date
        - gender: str
        - marital_status: str
        - address: str
        - phone_number: str
        - email: str
        - updated_by: int (This field will be added automatically by the system, so it is not necessary to send it in the request body)
        - company_id: int

    ## RESPONSE
        - Returns the updated person

    ## DEVELOPER NOTES
        - All fields are optional
        
    """

    result = persons.update(person, person_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(path="/persons{person_id}", status_code=status.HTTP_200_OK, summary="Delete Person")
async def delete_person(person_id: int, db_session: Session = Depends(get_db_connect)):
    """
    ## RESPONSE
        - Returns the deleted person
        
    """

    result = persons.delete(person_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)
