from app.models import Rabbit, RabbitCreate, RabbitUpdate

from .base import CRUDBase


class CRUDRabbit(CRUDBase[Rabbit, RabbitCreate, RabbitUpdate]):
    pass


rabbit = CRUDRabbit(Rabbit)
