import uvicorn
from dotenv import load_dotenv
from src.config.session import connect_to_db, get_data_base
from src.app import create_app
from fastapi import status

load_dotenv()



if __name__ == "__main__":
 
    engine = connect_to_db()

    get_data_base(engine)

    application = create_app()

    @application.get(path="/", status_code=status.HTTP_200_OK, tags=["server up"])
    async def server_start():
        """Server is up and running"""
        return {"message": "Welcome medical, server is up and running"}

    print("Starting server...")
    uvicorn.run(application, host="127.0.0.1", port=80, reload=False)