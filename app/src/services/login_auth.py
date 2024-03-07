from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text
from src.schemas.companies import CompanyRequest, CompanyUpdateRequest
# from src.utils.ctes import COMPANIES_ROW
from src.utils.helper import rows_to_dicts
from datetime import datetime

def get_user_info(db_session: Session, username: str) -> tuple:
    """Get User name and Password"""
    try:
        query = text("SELECT username, password, email FROM users WHERE username = :username")
        user = db_session.execute(query, {"username": username}).fetchone()

        print(f'user: {user}')
        
        return user[0], user[1], user[2]

    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex