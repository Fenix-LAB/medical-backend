# from app.src.models import Base


# async def create_tables(engine):
#     print("Creating tables...")
#     async with engine.begin() as conn:
#         print(f"conn: {conn}")
#         await conn.run_sync(Base.metadata.create_all)
#         print("Base.metadata:")
#     await engine.dispose()

from sqlalchemy.ext.automap import automap_base

from src.config.session import get_session, engine

# async def create_tables():
#     print("Creating tables...")
#     Base = automap_base()
#     Base.prepare(engine, reflect=True)

#     companies = Base.classes.companies

#     print(companies)

async def create_tables_async():
    async with get_session() as session:
        Base = automap_base()
        # Base.prepare(engine, reflect=True)
        
        
        await session.run_sync(Base.prepare(engine, reflect=True))
        companies = Base.classes.companies
        print(companies)

