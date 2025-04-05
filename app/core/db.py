from sqlmodel import create_engine, SQLModel
from .config import settings

connect_args = {"check_same_thread": False}
engine = create_engine(settings.DB_PATH, echo=True, connect_args=connect_args)


def init_db():
    SQLModel.metadata.create_all(engine)
