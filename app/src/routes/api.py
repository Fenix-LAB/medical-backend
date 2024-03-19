from fastapi import APIRouter, status

from .router import (
    companies,
    persons,
    disease_types,
    exam_types,
    exams,
    image_exams,
    images_types,
    services,
    diseases,
    establishment,
    users,
    login,
    appointments,
    doctors,
    insurances
)

router = APIRouter()

@router.get(path="/", status_code=status.HTTP_200_OK, tags=["server up"])
async def server_start():
    """Server is up and running"""
    return {"message": "Welcome medical, server is up and running"}

router.include_router(login.router, tags=["login"])
router.include_router(users.router, tags=["users"])
router.include_router(companies.router, tags=["companies"])
router.include_router(persons.router, tags=["persons"])
router.include_router(disease_types.router, tags=["disease_types"])
router.include_router(exam_types.router, tags=["exam_types"])
router.include_router(exams.router, tags=["exams"])
router.include_router(image_exams.router, tags=["image_exams"])
router.include_router(images_types.router, tags=["images_types"])
router.include_router(services.router, tags=["services"])
router.include_router(diseases.router, tags=["diseases"])
router.include_router(establishment.router, tags=["establishment"])