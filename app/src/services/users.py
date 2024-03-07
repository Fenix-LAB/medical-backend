from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from src.schemas.users import UserRequest, UserUpdateRequest
from src.utils.ctes import USERS_ROW
from src.utils.helper import rows_to_dicts
from datetime import datetime


def get(db_session: Session):
    """Get All Users"""
    try:
        query = text("SELECT * FROM users")
        users = db_session.execute(query).fetchall()

        # Convert the list of tuples to a list of dictionaries
        users = rows_to_dicts(users, USERS_ROW)
        
        return users

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def create(user: UserRequest, db_session: Session):
    """Create User"""
    try:
        # Generate the current datetime
        created_at = datetime.now()
        updated_at = datetime.now()

        data_user = {
            "username": user.username,
            "password": user.password,
            "email": user.email,
            "full_name": user.full_name,
            "role": user.role,
            "status": user.status,
            "created_by": user.created_by,
            "updated_by": user.updated_by,
            "created_at": created_at,
            "updated_at": updated_at
        }

        query = text("INSERT INTO users (username, password, email, full_name, role, status, created_by, updated_by, created_at, updated_at) VALUES (:username, :password, :email, :full_name, :role, :status, :created_by, :updated_by, :created_at, :updated_at)")

        db_session.execute(query, data_user)

        db_session.commit()

        return {"message": "User created successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def update(user: UserUpdateRequest, user_id: int, db_session: Session):
    """Update User"""
    try:
        # Generate the current datetime
        updated_at = datetime.now()

        data_user = {
            "username": user.username,
            "password": user.password,
            "email": user.email,
            "full_name": user.full_name,
            "role": user.role,
            "status": user.status,
            "updated_by": user.updated_by,
            "updated_at": updated_at
        }

        query = text("UPDATE users SET username = :username, password = :password, email = :email, full_name = :full_name, role = :role, status = :status, updated_by = :updated_by, updated_at = :updated_at WHERE id = :id")

        db_session.execute(query, {**data_user, "id": user_id})

        db_session.commit()

        return {"message": "User updated successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex
    

def delete(user_id: int, db_session: Session):
    """Delete User"""
    try:
        query = text("DELETE FROM users WHERE id = :id")
        db_session.execute(query, {"id": user_id})
        db_session.commit()

        return {"message": "User deleted successfully"}

    except Exception as ex:
        db_session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex