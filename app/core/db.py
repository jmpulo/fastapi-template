from sqlmodel import SQLModel, create_engine

from .config import settings


engine = create_engine(
    settings.DB_PATH,
    echo=True,
)


def init_db():
    SQLModel.metadata.create_all(engine)
