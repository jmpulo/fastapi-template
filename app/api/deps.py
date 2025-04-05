from typing import Generator

from sqlmodel import Session

from app.core.db import engine


def get_db() -> Generator:
    with Session(engine) as session:
        yield session
