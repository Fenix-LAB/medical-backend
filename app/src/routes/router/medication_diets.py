from fastapi import APIRouter
from fastapi import APIRouter, Depends, HTTPException, status, Header
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import medication_diets
from fastapi.responses import JSONResponse
from src.schemas.medication_diets import MedicationDietsRequest, MedicationDietsUpdateRequest
from src.utils.security import verify_token, valid_user
from src.utils.security import oauth2_scheme


router = APIRouter()

@router.get(path="/medication_diets", status_code=status.HTTP_200_OK, summary="Get All Medication Diets")
async def get_medication_diets(db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)):
    """
    ## RESPONSE
        - Returns a list of medication diets

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = medication_diets.get(db_session)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.post(path="/medication_diets", status_code=status.HTTP_201_CREATED, summary="Create Medication Diet")
async def create_medication_diet(medication_diet: MedicationDietsRequest, db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)):
    """
    ## REQUEST BODY
        - medication_type_id: int
        - company_id: int
        - medication_diet_name: str
        - generic_composition: str
        - indications: str
        - contraindications: str

    ## RESPONSE
        - Returns the created medication diet

    ## DEVELOPER NOTES
        - The company_id is a field that is required
        - The medication_type_id is a field that is required

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = medication_diets.create(medication_diet, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_201_CREATED)


@router.put(path="/medication_diets/{medication_diet_id}", status_code=status.HTTP_200_OK, summary="Update Medication Diet")
async def update_medication_diet(medication_diet: MedicationDietsUpdateRequest, medication_diet_id: int,  db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)):
    """
    ## REQUEST BODY
        - medication_type_id: int (optional)
        - company_id: int (optional)
        - medication_diet_name: str (optional)
        - generic_composition: str (optional)
        - indications: str (optional)
        - contraindications: str (optional)
        - status: int (optional)

    ## RESPONSE
        - Returns the updated medication diet

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = medication_diets.update(medication_diet, medication_diet_id, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)


@router.delete(path="/medication_diets/{medication_diet_id}", status_code=status.HTTP_200_OK, summary="Delete Medication Diet")
async def delete_medication_diet(medication_diet_id: int, db_session: Session = Depends(get_db_connect), token: str = Depends(oauth2_scheme)):
    """
    ## RESPONSE
        - Returns a message that the medication diet has been deleted

    """

    payload = verify_token(token)
    if isinstance(payload, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(payload))
    
    valid = valid_user(db_session, payload)
    if isinstance(valid, Exception):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=str(valid))

    result = medication_diets.delete(medication_diet_id, db_session, payload)
    if isinstance(result, Exception):
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(result))
    
    return JSONResponse(content=result, status_code=status.HTTP_200_OK)