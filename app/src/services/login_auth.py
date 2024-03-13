from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text

def get_user_info(db_session: Session, username: str) -> tuple:
    """Get User name, email and Password"""
    # try:
    query = text("SELECT username, password, email, user_id FROM users WHERE username = :username")
    user = db_session.execute(query, {"username": username}).fetchone()
    print(f'User: {user}')

    if user is None:
        return None, None, None, None

    return user

    # except Exception as ex:
    #     raise HTTPException(
    #         status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    #         detail=f'Error: {str(ex)}',
    #     ) from ex