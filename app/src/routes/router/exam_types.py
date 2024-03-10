from fastapi import APIRouter
from fastapi import APIRouter, Body, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import exam_types
from fastapi.responses import JSONResponse
from src.schemas.exam_types import ExamTypesRequest, ExamTypesUpdateRequest
from src.utils.security import verify_token, valid_user

router = APIRouter()

@router.get(path="/exam_types", status_code=status.HTTP_200_OK, summary="Get All Exam Types")
async def get_exam_types(db_session: Session = Depends(get_db_connect), token: str = Header(..., alias="x-token")):
    """
    ## RESPONSE
        - Returns a list of exam types

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = exam_types.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK) 


@router.post(path="/exam_types", status_code=status.HTTP_201_CREATED, summary="Create Exam Type")
async def create_exam_type(exam_type: ExamTypesRequest, db_session: Session = Depends(get_db_connect), token: str = Header(..., alias="x-token")):
    """
    ## REQUEST BODY
        - company_id: int
        - exam_name: str
        - description: str (optional)
        - status: int
        - created_by: int
        - updated_by: int (This field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the created exam type

    ## DEVELOPER NOTES
        - The description is a field that is optional

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = exam_types.create(exam_type, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/exam_types/{exam_type_id}", status_code=status.HTTP_200_OK, summary="Update Exam Type")
async def update_exam_type(exam_type: ExamTypesUpdateRequest, exam_type_id: int, db_session: Session = Depends(get_db_connect), token: str = Header(..., alias="x-token")):
    """
    ## REQUEST BODY
        - company_id: int (optional)
        - exam_name: str (optional)
        - description: str (optional)
        - status: int (optional)
        - updated_by: int (optional, this field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the updated exam type

    ## DEVELOPER NOTES
        - All fields are optional
        
    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = exam_types.update(exam_type, exam_type_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(path="/exam_types/{exam_type_id}", status_code=status.HTTP_200_OK, summary="Delete Exam Type")
async def delete_exam_type(exam_type_id: int, db_session: Session = Depends(get_db_connect), token: str = Header(..., alias="x-token")):
    """
    ## REQUEST PARAMS
        - exam_type_id: int

    ## RESPONSE
        - Returns the deleted exam type

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = exam_types.delete(exam_type_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)