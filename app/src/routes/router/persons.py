from fastapi import APIRouter
from fastapi import APIRouter, Body, Depends, Header, HTTPException, status
from sqlalchemy.orm import Session
from src.config.get_session import get_db_connect
from src.services import companies
from fastapi.responses import JSONResponse
from src.schemas.persons import PersonsRequest, PersonsUpdateRequest

router = APIRouter()

@router.get(path="/persons", status_code=status.HTTP_200_OK, summary="Get All Persons")