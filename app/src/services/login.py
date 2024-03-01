from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Any
from src.utils import passutil

def check_username_password(email: str, password: str, db: Session) -> Any:
    """ Verify Password"""
    db_user_info = get_user(email=email, db=db)

    return passutil.verify_password(str(password), str(db_user_info.password))

def check_active_session(session_id: str, db: Session):
    """ check for active session """
    try:
        db_session = db.query(models.UsersLoginAttempt).filter(
            models.UsersLoginAttempt.session_id == session_id).first()

        return db_session
    except SQLAlchemyError as e:
        fastapi_logger.exception("logoff_user")
        return None

def login_user(user: schemas.UserLogIn, session_id: str, Sdb: Session) -> Any:
    """ Login Attempt Record """
    try:
        db_session = models.UsersLoginAttempt(
            email=user.email,
            session_id=session_id,
            ip_address=user.ip_address,
            browser=user.browser,
            status="logged_in")
        db.add(db_session)
        db.commit()
        db.refresh(db_session)
        return db_session
    except SQLAlchemyError as e:
        fastapi_logger.exception("login_user")
        return None

def active_user(session_id: str, db: Session) -> Any:
    """ check for active user"""
    try:
        db_session = db.query(models.UsersLoginAttempt).filter(
            models.UsersLoginAttempt.session_id == session_id).first()

        db_session.status = "active"
        db.commit()
        db.refresh(db_session)
        return db_session
    except SQLAlchemyError as e:
        fastapi_logger.exception("active_user")
        return None

def logoff_user(self, session_id: str, db: Session) -> Any:
    """ Logging off Record"""
    try:
        db_session = db.query(models.UsersLoginAttempt).filter(
            models.UsersLoginAttempt.session_id == session_id).first()

        db_session.status = "logged_off"
        db.commit()
        db.refresh(db_session)
        return db_session
    except SQLAlchemyError as e:
        fastapi_logger.exception("logoff_user")
        return None