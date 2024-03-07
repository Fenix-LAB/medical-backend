from fastapi import APIRouter
from fastapi import APIRouter, Body, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import users
from fastapi.responses import JSONResponse
from src.schemas.users import UserRequest, UserUpdateRequest

router = APIRouter()

@router.get(path="/users", status_code=status.HTTP_200_OK, summary="Get All Users")
async def get_users(db_session: Session = Depends(get_db_connect)):
    """
    ## RESPONSE
        - Returns a list of users

    """

    result = users.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/users", status_code=status.HTTP_201_CREATED, summary="Create User")
async def create_user(user: UserRequest, db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST BODY
        - username: str
        - password: str
        - email: str
        - full_name: str
        - role: str
        - status: int
        - created_by: int
        - updated_by: int (This field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the created user

    ## DEVELOPER NOTES
        - The contact_person_id is a field that is optional

    """

    result = users.create(user, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/users{user_id}", status_code=status.HTTP_200_OK, summary="Update User")
async def update_user(user: UserUpdateRequest, user_id: int,  db_session: Session = Depends(get_db_connect)):
    """
    ## REQUEST BODY
        - username: str (optional)
        - password: str (optional)
        - email: str (optional)
        - full_name: str (optional)
        - role: str (optional)
        - status: int (optional)
        - updated_by: int (optional, this field will be added automatically by the system, so it is not necessary to send it in the request body)

    ## RESPONSE
        - Returns the updated user

    """
    result = users.update(user, user_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(path="/users{user_id}", status_code=status.HTTP_200_OK, summary="Delete User")
async def delete_user(user_id: int, db_session: Session = Depends(get_db_connect)):
    """
    ## RESPONSE
        - Returns the deleted user

    """

    result = users.delete(user_id, db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)
