from contextlib import contextmanager
from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker


# Database connection
host = "localhost"
port = "5432"
user = "postgres"
password = "medical"
db_name = "medical_db"

POSTGRES_SQL_CONNECTION = (
    f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
)

try:
    engine = create_engine(POSTGRES_SQL_CONNECTION, echo=True)
    print("Conection to Database was successful!")
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

except Exception as ex:
    print("Could Not connect to Database %s", ex)

