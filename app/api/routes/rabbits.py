from fastapi import APIRouter, HTTPException, status, Depends
from sqlmodel import Session
from uuid import UUID
from app.models import RabbitCreate, RabbitPublic, RabbitUpdate

from app.api import deps
from app import crud

router = APIRouter()


@router.get("/", response_model=list[RabbitPublic])
async def read_rabbits(*, db: Session = Depends(deps.get_db)):
    """Retrieve Rabbits"""
    return crud.rabbit.get_multi(db)


@router.get("/{rabbit_id}", response_model=RabbitPublic)
async def read_rabbit(*, db: Session = Depends(deps.get_db), rabbit_id: UUID):
    """Retrieve Rabbit by id"""
    return crud.rabbit.get(db, id=rabbit_id)


@router.post("/", response_model=RabbitPublic)
async def create_rabbit(*, db: Session = Depends(deps.get_db), obj_in: RabbitCreate):
    """Create new Rabbit"""
    return crud.rabbit.create(db, obj_in=obj_in)


@router.put("/{rabbit_id}", response_model=RabbitPublic)
async def update_rabbit(
    *,
    db: Session = Depends(deps.get_db),
    rabbit_id: UUID,
    obj_in: RabbitUpdate,
):
    """Update an existing Rabbit"""
    rabbit = crud.rabbit.get(db, id=rabbit_id)
    if not rabbit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Rabbit not found"
        )
    return crud.rabbit.update(db, db_obj=rabbit, obj_in=obj_in)


@router.delete("/{rabbit_id}", response_model=RabbitPublic)
async def delete_rabbit(
    *,
    db: Session = Depends(deps.get_db),
    rabbit_id: UUID,
):
    """Delete a Rabbit"""
    rabbit = crud.rabbit.get(db, id=rabbit_id)
    if not rabbit:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Rabbit not found"
        )
    return crud.rabbit.remove(db, id=rabbit_id)
