from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(
    title="Container Manamagement Application",
    description="API for managing demurrage and detention fees for shipping containers.",
    version="1.0.0"
)

app.include_router(endpoints.router)
