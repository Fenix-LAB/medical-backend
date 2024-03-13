from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.utils.security import create_access_token
from src.services.login_auth import get_user_info
from src.config.get_session import get_db_connect
from fastapi.responses import JSONResponse
from fastapi import HTTPException, status

router = APIRouter()

# Ruta para autenticar usuarios y obtener un token JWT
@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(get_db_connect)):

    user_db, password_db, email_db, id_db = get_user_info(db_session, form_data.username)
    
    if user_db is None or password_db != form_data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"}
    )
    else:
        access_token = create_access_token(data={"sub": user_db, "email": email_db, "id": id_db})
        return JSONResponse(content={"access_token": access_token, "token_type": "bearer", "info": "Token has been created successfully"})
