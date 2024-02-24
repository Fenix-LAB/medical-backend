from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

# Database connection
host = "localhost"
port = "5432"
user = "postgres"
password = "medical"
db_name = "medical_db"

POSTGRES_SQL_CONNECTION = (
    f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{db_name}"
)

try:
    engine = create_async_engine(POSTGRES_SQL_CONNECTION, echo=True)
    print("Conection succesfully")
except Exception as ex:
    print("Could Not connect to Database %s", ex)


async_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


@asynccontextmanager
async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session() as session:
        async with session.begin():
            try:
                yield session
            finally:
                await session.close()
