from sqlmodel import create_engine

from alembic import command
from alembic.config import Config

from .config import settings

engine = create_engine(
    settings.DB_PATH,
    echo=True,
)


def init_db():

    alembic_cfg = Config("alembic.ini")
    command.upgrade(alembic_cfg, "head")
