from sqlmodel import Session
from typing import Dict
from app.models import RabbitCreate
from app import crud


def test_create_rabbit(db: Session, new_rabbit_create: RabbitCreate) -> None:
    db_obj = crud.rabbit.create(db=db, obj_in=new_rabbit_create)
    assert db_obj.id is not None
    assert db_obj.color == new_rabbit_create.color
    assert db_obj.location == new_rabbit_create.location
