from typing import Dict, Generator

import pytest
from faker import Faker
from fastapi.testclient import TestClient
from sqlmodel import Session

from app import crud
from app.core.db import engine, init_db
from app.main import app
from app.models import RabbitCreate
from app.tests.utils import body_part_provider

fake = Faker()
fake.add_provider(body_part_provider)


@pytest.fixture(scope="session")
def db() -> Generator:
    """Create a new database session for a test."""
    init_db()
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="session")
def client() -> Generator:
    """Create a new FastAPI test client."""
    with TestClient(app) as c:
        yield c


@pytest.fixture()
def new_rabbit_dict() -> Dict:
    """Create a new Rabbit dictionary for testing."""
    return {
        "color": fake.color_name(),
        "location": fake.body_part(),
    }


@pytest.fixture()
def new_rabbit_create(new_rabbit_dict: Dict) -> RabbitCreate:
    """Create a new RabbitCreate object for testing."""
    return RabbitCreate(**new_rabbit_dict)


@pytest.fixture()
def new_rabbit_db(db: Session, new_rabbit_create: RabbitCreate) -> None:
    """Create a new Rabbit in the database for testing."""
    return crud.rabbit.create(db=db, obj_in=new_rabbit_create)
