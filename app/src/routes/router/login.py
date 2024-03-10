from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.utils.security import create_access_token
from src.services.login_auth import get_user_info
from src.config.get_session import get_db_connect
from fastapi.responses import JSONResponse

router = APIRouter()

# Ruta para autenticar usuarios y obtener un token JWT
@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(get_db_connect)):
    user_db, password_db, email_db = get_user_info(db_session, form_data.username)

    if not user_db or form_data.password != password_db:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    access_token = create_access_token(data={"sub": user_db, "email": email_db})
    return JSONResponse(content={"access_token": access_token, "token_type": "bearer", "info": "Token has been created successfully"})
