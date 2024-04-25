from contextlib import contextmanager
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from .database import DATABASE_HOST, DATABASE_PORT, DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME


POSTGRES_SQL_CONNECTION = (
    f"postgresql://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"
)

try:
    engine = create_engine(POSTGRES_SQL_CONNECTION, echo=True)
    print("Conection to Database was successful!")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

except Exception as ex:
    print("Could Not connect to Database %s", ex)

