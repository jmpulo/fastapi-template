import uuid

from sqlmodel import Field, SQLModel


class RabbitBase(SQLModel):
    color: str = "White"
    location: str | None = Field(default=None, max_length=20)


class Rabbit(RabbitBase, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)


class RabbitCreate(RabbitBase):
    pass


class RabbitUpdate(RabbitBase):
    pass


class RabbitPublic(RabbitBase):
    id: uuid.UUID
