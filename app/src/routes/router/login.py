from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError

app = FastAPI()

# Secret key para firmar los tokens JWT (debería ser una clave secreta más segura en un entorno de producción)
SECRET_KEY = "43611869c1ed09fe5388ecbc8b3eab582f2c5c4fe22a2ed8de1fe9455c10267c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Simulación de una base de datos de usuarios
fake_users_db = {
    "user1": {
        "username": "user1",
        "full_name": "User One",
        "email": "user1@example.com",
        "hashed_password": "fakehashedpassword",
        "disabled": False,
    }
}

# Función para generar un token JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Dependencia para obtener el token JWT de la cabecera de autorización
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Ruta para autenticar usuarios y obtener un token JWT
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or form_data.password != "password":
        raise HTTPException(status_code=400, detail="Incorrect username or password")
    access_token = create_access_token(data={"sub": user["username"], "email": user["email"]})
    return {"access_token": access_token, "token_type": "bearer"}

# Ruta protegida que requiere autenticación mediante token JWT
@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # print(payload)
        username: str = payload.get("sub")
        email: str = payload.get("email")  # Obtener el correo electrónico del payload del token
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": "This is a protected route", "username": username, "email": email}
