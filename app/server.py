import asyncio
import uvicorn
from dotenv import load_dotenv

from src.app import create_app
# from src.config.pupulate import create_tables
from src.config.pupulate import create_tables_async
# from src.db.session import engine

load_dotenv()

application = create_app()

if __name__ == "__main__":
    print("Populating database...")
    # try:
    #     asyncio.run(create_tables())
    #     print("Database populated.")
    # except Exception as ex:
    #     print("Error creating tables %s", ex)

    asyncio.run(create_tables_async())

    print("Starting server...")
    uvicorn.run("main:application", host="127.0.0.1", port=8000, reload=True)