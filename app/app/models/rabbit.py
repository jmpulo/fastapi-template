from sqlmodel import Field,SQLModel

class RabbitBase(SQLModel):
    color:str="White"
    location:str|None=Field(default="Neck",max_length=20)

class RabbitCreate(RabbitBase):
    pass