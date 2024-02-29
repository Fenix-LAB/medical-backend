from fastapi import APIRouter, status

from .router import (
    companies,
    persons,
    disease_types,
    exam_types
)

router = APIRouter()

@router.get(path="/", status_code=status.HTTP_200_OK, tags=["server up"])
async def server_start():
    """Server is up and running"""
    return {"message": "Welcome medical, server is up and running"}

router.include_router(companies.router, tags=["companies"])
router.include_router(persons.router, tags=["persons"])
router.include_router(disease_types.router, tags=["disease_types"])
router.include_router(exam_types.router, tags=["exam_types"])

