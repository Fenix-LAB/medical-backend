from fastapi import APIRouter
from fastapi import APIRouter, Body, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import image_exams
from fastapi.responses import JSONResponse
from src.schemas.image_exams import ImageExamRequest, ImageExamUpdateRequest

router = APIRouter()

@router.get(path="/image_exams", status_code=status.HTTP_200_OK, summary="Get All Image Exams")
async def get_image_exams(db_session: Session = Depends(get_db_connect)):
    """
    ## RESPONSE
        - Returns a list of image exams

    """

    result = image_exams.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/image_exams", status_code=status.HTTP_201_CREATED, summary="Create Image Exam")
async def create_image_exam(image_exam: ImageExamRequest, db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST BODY
        - image_type_id: int (optional)
        - company_id: int (optional)
        - exam_name: str
        - description: str (optional)
        - status: int
        - created_by: int
        - updated_by: int (This field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the created image exam

    ## DEVELOPER NOTES
        - The image_type_id and company_id are fields that are optional

    """
    
    result = image_exams.create(image_exam, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/image_exams{image_exam_id}", status_code=status.HTTP_200_OK, summary="Update Image Exam")
async def update_image_exam(image_exam: ImageExamUpdateRequest, image_exam_id: int,  db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST BODY
        - image_type_id: int (optional)
        - company_id: int (optional)
        - exam_name: str (optional)
        - description: str (optional)
        - status: int (optional)
        - updated_by: int (optional, this field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the updated image exam

    ## DEVELOPER NOTES
        - The image_type_id, company_id, exam_name and description are fields that are optional

    """

    result = image_exams.update(image_exam, image_exam_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(path="/image_exams{image_exam_id}", status_code=status.HTTP_200_OK, summary="Delete Image Exam")
async def delete_image_exam(image_exam_id: int, db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST PARAMS
        - image_exam_id: int

    ## RESPONSE
        - Returns the deleted image exam

    """

    result = image_exams.delete(image_exam_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)