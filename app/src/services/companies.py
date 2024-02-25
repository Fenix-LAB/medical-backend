from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from sqlalchemy import text

def get(db_session: Session):
    """Get All Companies"""
    try:
        print("Starting get...")
        print(f"db_session: {db_session}")
        query = text("SELECT * FROM companies")
        companies = db_session.execute(query).fetchall()
        print(f"Companies: {companies}")
        return companies
    except Exception as ex:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(ex),
        ) from ex