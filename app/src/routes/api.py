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
    insurances,
    medication_types,
    medication_diets,
    medical_attention,
    patients,
    specialties
)

router = APIRouter()

@router.get(path="/", status_code=status.HTTP_200_OK, tags=["server up"])
async def server_start():
    """Server is up and running"""
    return {"message": "Welcome medical, server is up and running"}

router.include_router(appointments.router, tags=["appointments"])
router.include_router(companies.router, tags=["companies"])
router.include_router(disease_types.router, tags=["disease_types"])
router.include_router(diseases.router, tags=["diseases"])
router.include_router(doctors.router, tags=["doctors"])
router.include_router(establishment.router, tags=["establishment"])
router.include_router(exam_types.router, tags=["exam_types"])
router.include_router(exams.router, tags=["exams"])
router.include_router(image_exams.router, tags=["image_exams"])
router.include_router(images_types.router, tags=["images_types"])
router.include_router(insurances.router, tags=["insurances"])
router.include_router(login.router, tags=["login"])
router.include_router(medical_attention.router, tags=["medical_attention"])
router.include_router(medication_diets.router, tags=["medication_diets"])
router.include_router(medication_types.router, tags=["medication_types"])
router.include_router(patients.router, tags=["patients"])
router.include_router(persons.router, tags=["persons"])
router.include_router(services.router, tags=["services"])
router.include_router(specialties.router, tags=["specialties"])
router.include_router(users.router, tags=["users"])