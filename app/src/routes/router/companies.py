from fastapi import APIRouter
from fastapi import APIRouter, Body, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import companies
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get(path="/companies", status_code=status.HTTP_200_OK)
async def get_companies(
    db_session: Session = Depends(get_db_connect)
):
    """Get all companies"""
    print("Starting get_companies...")
    result = companies.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)