from sqlmodel import Field,SQLModel
import uuid

class RabbitBase(SQLModel):
    color:str="White"
    location:str|None=Field(default="Neck",max_length=20)

class RabbitCreate(RabbitBase):
    pass

class Rabbit(RabbitBase,table=True):
    id:str = Field(default=lambda: str(uuid.uuid4()), nullable=False, primary_key=True)

