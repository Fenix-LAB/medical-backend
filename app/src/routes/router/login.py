from fastapi import Depends, HTTPException, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from src.utils.security import create_access_token
from src.services.login_auth import get_user_info
from src.config.get_session import get_db_connect

router = APIRouter()

# Dependencia para obtener el token JWT de la cabecera de autorización
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Ruta para autenticar usuarios y obtener un token JWT
@router.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db_session: Session = Depends(get_db_connect)):
    user_db, password_db, email_db = get_user_info(db_session, form_data.username)

    if not user_db or form_data.password != password_db:
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    
    access_token = create_access_token(data={"sub": user_db, "email": email_db})
    return {"access_token": access_token, "token_type": "bearer"}

# Ruta protegida que requiere autenticación mediante token JWT
# @router.get("/protected")
# async def protected_route(token: str = Depends(oauth2_scheme)):
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         # print(payload)
#         username: str = payload.get("sub")
#         email: str = payload.get("email")  # Obtener el correo electrónico del payload del token
#         if username is None:
#             raise HTTPException(status_code=401, detail="Invalid authentication credentials")
#     except JWTError:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return {"message": "This is a protected route", "username": username, "email": email}
