from fastapi import APIRouter

from app.api.routes import rabbits

api_router = APIRouter()
api_router.include_router(rabbits.router, prefix="/rabbits")
