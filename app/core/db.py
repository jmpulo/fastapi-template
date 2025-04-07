from sqlmodel import SQLModel, create_engine

from .config import settings

# connect_args = {"check_same_thread": False}
# , connect_args=connect_args
engine = create_engine(settings.DB_PATH, echo=True)


def init_db():
    SQLModel.metadata.create_all(engine)
