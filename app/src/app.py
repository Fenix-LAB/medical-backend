from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.api import router


def create_app():
    app = FastAPI(title="Medical API", version="0.1.0", description="Medical API for software SAAS for medical clinics")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    app.include_router(router, prefix="/api/v1")

    return app