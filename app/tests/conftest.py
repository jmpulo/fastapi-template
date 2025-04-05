from fastapi.testclient import TestClient
from typing import Generator
from app.main import app
from app.models import RabbitCreate
from sqlmodel import Session
from app.core.db import engine
from faker import Faker
from typing import Dict
import pytest

fake = Faker()


@pytest.fixture(scope="session")
def db() -> Generator:
    """Create a new database session for a test."""
    with Session(engine) as session:
        yield session


@pytest.fixture(scope="module")
def client() -> Generator:
    """Create a new FastAPI test client."""
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="session")
def new_rabbit_dict() -> Dict:
    """Create a new Rabbit dictionary for testing."""
    return {
        "color": fake.color_name(),
        "location": fake.body_part(),
    }


@pytest.fixture(scope="session")
def new_rabbit_create(new_rabbit_dict: Dict) -> RabbitCreate:
    """Create a new RabbitCreate object for testing."""
    return RabbitCreate(**new_rabbit_dict)
