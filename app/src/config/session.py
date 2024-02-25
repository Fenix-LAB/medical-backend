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

def connect_to_db():

    try:
        engine = create_engine(POSTGRES_SQL_CONNECTION, echo=True)
        print("Conection succesfully")
    except Exception as ex:
        print("Could Not connect to Database %s", ex)

    return engine


def get_data_base(engine):
    meta = MetaData() 

    meta.reflect(bind=engine)

    Base = declarative_base() 

    for table_name in meta.tables:
        print("Table name:", table_name)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    return SessionLocal


