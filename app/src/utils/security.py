import jwt
from datetime import datetime, timedelta
from typing import Optional

# Secret key para firmar los tokens JWT (debería ser una clave secreta más segura en un entorno de producción)
SECRET_KEY = "43611869c1ed09fe5388ecbc8b3eab582f2c5c4fe22a2ed8de1fe9455c10267c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
#TODO: Mover a archivo .env

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