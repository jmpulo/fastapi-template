from typing import Dict

from fastapi import status
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.core.config import settings
from app.models import Rabbit
from app.tests.conftest import fake
from app.tests.utils import generate_unique

base_url = f"{settings.API_V1_STR}/rabbits"


def test_create_rabbit(client: TestClient, db: Session, new_rabbit_dict: Dict) -> None:
    res = client.post(url=base_url, json=new_rabbit_dict)
    assert res.status_code == status.HTTP_200_OK
    content = res.json()
    assert content["color"] == new_rabbit_dict["color"]
    assert content["location"] == new_rabbit_dict["location"]


def test_read_rabbit(client: TestClient, db: Session, new_rabbit_db: Rabbit) -> None:
    res = client.get(url=f"{base_url}/{new_rabbit_db.id}")
    assert res.status_code == status.HTTP_200_OK
    content = res.json()
    assert content["id"] == str(new_rabbit_db.id)
    assert content["color"] == new_rabbit_db.color
    assert content["location"] == new_rabbit_db.location


def test_read_rabbits(client: TestClient, db: Session, new_rabbit_db: Rabbit) -> None:
    res = client.get(url=base_url)
    assert res.status_code == status.HTTP_200_OK

    content = res.json()
    assert len(content) > 0

    found = False
    count = 0
    while not found and count < len(content):
        if content[count]["id"] == str(new_rabbit_db.id):
            found = True
        count += 1

    assert found


def test_update_rabbit(client: TestClient, db: Session, new_rabbit_db: Rabbit) -> None:
    new_color = generate_unique(new_rabbit_db.color, fake.color_name)
    new_location = generate_unique(new_rabbit_db.location, fake.body_part)

    res = client.put(
        url=f"{base_url}/{new_rabbit_db.id}",
        json={
            "color": new_color,
            "location": new_location,
        },
    )
    assert res.status_code == status.HTTP_200_OK
    content = res.json()
    assert content["id"] == str(new_rabbit_db.id)
    assert content["color"] != new_rabbit_db.color
    assert content["location"] != new_rabbit_db.location

    # Test partial update

    old_rabbit = content.copy()
    new_color = generate_unique(old_rabbit["color"], fake.color_name)
    data = {
        "color": new_color,
    }
    res = client.put(
        url=f"{base_url}/{new_rabbit_db.id}",
        json=data,
    )
    assert res.status_code == status.HTTP_200_OK
    content = res.json()

    assert content["id"] == old_rabbit["id"]
    assert content["color"] != old_rabbit["color"]
    assert content["location"] == old_rabbit["location"]


def test_delete_rabbit(client: TestClient, db: Session, new_rabbit_db: Rabbit) -> None:
    res = client.delete(url=f"{base_url}/{new_rabbit_db.id}")
    assert res.status_code == status.HTTP_200_OK
    content = res.json()

    assert content["id"] == str(new_rabbit_db.id)
    assert content["color"] == new_rabbit_db.color
    assert content["location"] == new_rabbit_db.location

    # Check if the rabbit is deleted from the database
    res = client.get(url=f"{base_url}/{new_rabbit_db.id}")
    assert res.status_code == status.HTTP_404_NOT_FOUND
