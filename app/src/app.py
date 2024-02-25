from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.api import router


def create_app():
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost", "http://localhost:3000"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    print("Starting router...")
    app.include_router(router, prefix="/api/v1")

    return app