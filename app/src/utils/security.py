import jwt
from datetime import datetime, timedelta
from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy import text
from fastapi.security import OAuth2PasswordBearer

# Secret key para firmar los tokens JWT (debería ser una clave secreta más segura en un entorno de producción)
SECRET_KEY = "43611869c1ed09fe5388ecbc8b3eab582f2c5c4fe22a2ed8de1fe9455c10267c"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
#TODO: Mover a archivo .env
# Dependencia para obtener el token JWT de la cabecera de autorización
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Función para generar un token JWT
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Función para generar un token JWT
    :param data: dict: Datos que se incluirán en el token
    :param expires_delta: timedelta: Tiempo de expiración del token
    :return: str: Token JWT
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str):
    """
    Función para verificar un token JWT
    :param token: str: Token JWT
    :return: tuple: Retorna una tupla con el usuario y el correo electrónico del token
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return "Token has expired"
    except jwt.InvalidTokenError:
        return "Invalid token"
    except Exception as e:
        return e
    
def valid_user(db_session: Session, payload):
    """
    Función para obtener la información de un usuario
    :param db_session: Session: Sesión de la base de datos
    :param payload: dict: Payload del token JWT
    :return: bool: Retorna True si el usuario existe, de lo contrario False
    """
    username = payload.get("sub")
    try:
        query = text("SELECT username, password, email FROM users WHERE username = :username")
        db_session.execute(query, {"username": username}).fetchone()
        return f'User {username} is valid'
    except Exception as ex:
        return f'Error: {ex}'
       