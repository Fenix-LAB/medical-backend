from fastapi import APIRouter
from fastapi import APIRouter, Body, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import exams
from fastapi.responses import JSONResponse
from src.schemas.exams import ExamsRequest, ExamsUpdateRequest


router = APIRouter()

@router.get(path="/exams", status_code=status.HTTP_200_OK, summary="Get All Exams")
async def get_exams(db_session: Session = Depends(get_db_connect)):
    """
    ## RESPONSE
        - Returns a list of exams

    """

    result = exams.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/exams", status_code=status.HTTP_201_CREATED, summary="Create Exam")
async def create_exam(exam: ExamsRequest, db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST BODY
        - exam_type_id: int
        - company_id: int
        - exam_name: str
        - description: str (optional)
        - status: int
        - created_by: int
        - updated_by: int (This field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the created exam

    ## DEVELOPER NOTES
        - The description is a field that is optional

    """

    result = exams.create(exam, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/exams{exam_id}", status_code=status.HTTP_200_OK, summary="Update Exam")
async def update_exam(exam: ExamsUpdateRequest, exam_id: int,  db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST BODY
        - exam_type_id: int (optional)
        - company_id: int (optional)
        - exam_name: str (optional)
        - description: str (optional)
        - status: int (optional)
        - updated_by: int (optional, this field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the updated exam

    """

    result = exams.update(exam, exam_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(path="/exams{exam_id}", status_code=status.HTTP_200_OK, summary="Delete Exam")
async def delete_exam(exam_id: int, db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST PARAMS
        - exam_id: int

    ## RESPONSE
        - Returns the deleted exam

    """

    result = exams.delete(exam_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)