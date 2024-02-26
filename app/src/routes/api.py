from fastapi import APIRouter, status

from .router import (
    companies,
)

router = APIRouter()

@router.get(path="/", status_code=status.HTTP_200_OK, tags=["server up"])
async def server_start():
    """Server is up and running"""
    return {"message": "Welcome medical, server is up and running"}

router.include_router(companies.router, tags=["companies"])