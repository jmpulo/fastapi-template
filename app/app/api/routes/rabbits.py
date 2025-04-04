from fastapi import APIRouter,HTTPException,status,Depends
from sqlmodel import Session
from uuid import UUID
from app.models import Rabbit,RabbitCreate,RabbitPublic
from app.core.config import settings
from app.api import deps
from app import crud

router=APIRouter()

@router.get("/",response_model=list[RabbitPublic])
async def get_rabbit(*,db:Session=Depends(deps.get_db)):
    """Retrieve Rabbits"""
    return crud.rabbit.get_multi(db)

@router.get("/{rabbit_id}",response_model=RabbitPublic)
async def get_rabbit(*,db:Session=Depends(deps.get_db), rabbit_id:UUID):
    """Retrieve Rabbits"""
    return crud.rabbit.get(db,id=rabbit_id)

@router.post("/",response_model=RabbitPublic)
async def get_rabbit(*,db:Session=Depends(deps.get_db),obj_in:RabbitCreate):
    """Retrieve Rabbits"""
    return crud.rabbit.create(db,obj_in=obj_in)
    

