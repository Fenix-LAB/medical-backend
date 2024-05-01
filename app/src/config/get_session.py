# from src.config.session import connect_to_db
from contextlib import contextmanager

from sqlalchemy import MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

from src.config.session import SessionLocal

# SessionLocal = connect_to_db()


# @contextmanager
# def get_db_connect() -> SessionLocal:
#     """Provide a transactional scope around a series of operations."""
#     db = None
#     try:
#         print("Opening database connection...")
#         db = SessionLocal()  # create session from SQLAlchemy sessionmaker
#         yield db
#     finally:
#         print("Closing database connection...")
#         db.close()
def get_data_base(engine):
    meta = MetaData()

    meta.reflect(bind=engine)

    Base = declarative_base()

    # for table_name in meta.tables:
    #     print("Table name:", table_name)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return SessionLocal


# @contextmanager
def get_db_connect():
    """start connect db"""
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        db_session.close()
