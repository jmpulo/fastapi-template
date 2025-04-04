from typing import Generic, Type, TypeVar
from sqlmodel import SQLModel,Session,select

ModelType=TypeVar("ModelType", bound=SQLModel)
CreateModelType=TypeVar("CreateModelType", bound=SQLModel)
UpdateModelType=TypeVar("UpdateModelType", bound=SQLModel)



class CRUDBase(Generic[ModelType, CreateModelType, UpdateModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model=model

    def get(self, db:Session,id:str)-> ModelType | None:
        return db.get(self.model,id)

    def get_multi(self,db:Session)->list[ModelType]:
        return db.query(self.model).all()
    
    def create(self,db:Session,*,obj_in:CreateModelType)->ModelType:
        db_obj=self.model.model_validate(obj_in)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    
    def update(self,db:Session,*,db_obj:ModelType,obj_in:UpdateModelType)->ModelType:
        obj_data=obj_in.model_dump(exclude_unset=True)
        for key, value in obj_data.items():
            setattr(db_obj, key, value)
        
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def remove(self, db:Session,*,db_obj:ModelType)->ModelType:
        db.delete(db_obj)
        db.commit()
        return db_obj



