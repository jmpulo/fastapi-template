from fastapi import APIRouter
from app.models import RabbitCreate
from app.core.config import settings

router=APIRouter()

@router.get("/",response_model=RabbitCreate)
async def get_rabbit():
    """Retrieve Rabbits"""
    print(settings.DB_PATH)
    return RabbitCreate()
