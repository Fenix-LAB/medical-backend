from fastapi import APIRouter
from fastapi import APIRouter, Body, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import image_types
from fastapi.responses import JSONResponse
from src.schemas.image_type import ImageTypeRequest, ImageTypeUpdateRequest

router = APIRouter()

@router.get(path="/image_types", status_code=status.HTTP_200_OK, summary="Get All Image Types")
async def get_image_types(db_session: Session = Depends(get_db_connect)):
    """
    ## RESPONSE
        - Returns a list of image types

    """

    result = image_types.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/image_types", status_code=status.HTTP_201_CREATED, summary="Create Image Type")
async def create_image_type(image_type: ImageTypeRequest, db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST BODY
        - company_id: int (optional)
        - image_type_name: str
        - description: str (optional)
        - status: int
        - created_by: int
        - updated_by: int (This field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the created image type

    ## DEVELOPER NOTES
        - The company_id is a field that is optional

    """
    
    result = image_types.create(image_type, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/image_types/{image_type_id}", status_code=status.HTTP_200_OK, summary="Update Image Type")
async def update_image_type(image_type: ImageTypeUpdateRequest, image_type_id: int,  db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST BODY
        - company_id: int (optional)
        - image_type_name: str (optional)
        - description: str (optional)
        - status: int (optional)
        - updated_by: int (optional, this field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the updated image type

    """

    result = image_types.update(image_type, image_type_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(path="/image_types/{image_type_id}", status_code=status.HTTP_200_OK, summary="Delete Image Type")
async def delete_image_type(image_type_id: int, db_session: Session = Depends(get_db_connect)):
    """
    ## RESPONSE
        - Returns the deleted image type

    """

    result = image_types.delete(image_type_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK) 
