from fastapi import APIRouter

router = APIRouter()

@router.get("/companies")
async def get_companies():
    return {"companies": [{"name": "Company1"}, {"name": "Company2"}]}