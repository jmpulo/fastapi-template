from sqlmodel import Session

from app import crud
from app.models import Rabbit, RabbitCreate, RabbitUpdate
from app.tests.conftest import fake
from app.tests.utils import generate_unique


def test_create_rabbit(db: Session, new_rabbit_create: RabbitCreate) -> None:
    db_obj = crud.rabbit.create(db=db, obj_in=new_rabbit_create)

    assert db_obj.id is not None
    assert db_obj.color == new_rabbit_create.color
    assert db_obj.location == new_rabbit_create.location


def test_read_rabbit(db: Session, new_rabbit_db: Rabbit) -> None:
    db_obj = crud.rabbit.get(db=db, id=new_rabbit_db.id)

    assert db_obj is not None
    assert db_obj.id == new_rabbit_db.id
    assert db_obj.color == new_rabbit_db.color
    assert db_obj.location == new_rabbit_db.location


def test_update_rabbit(db: Session, new_rabbit_db: Rabbit) -> None:
    # Make sure the new color is different from the old one
    # to avoid a false positive

    new_color = generate_unique(new_rabbit_db.color, fake.color_name)
    assert new_rabbit_db.color != new_color
    old_color = new_rabbit_db.color

    db_obj = crud.rabbit.update(
        db=db, db_obj=new_rabbit_db, obj_in=RabbitUpdate(color=new_color)
    )
    assert db_obj.id == new_rabbit_db.id
    assert db_obj.color == new_color
    assert db_obj.color != old_color


def test_delete_rabbit(db: Session, new_rabbit_db: Rabbit) -> None:
    db_obj = crud.rabbit.remove(db=db, db_obj=new_rabbit_db)
    assert db_obj.id == new_rabbit_db.id
    assert db_obj.color == new_rabbit_db.color
    assert db_obj.location == new_rabbit_db.location

    # Check if the rabbit is deleted from the database
    db_obj = crud.rabbit.get(db=db, id=new_rabbit_db.id)
    assert db_obj is None
