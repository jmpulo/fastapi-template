from .base import CRUDBase
from app.models import Rabbit, RabbitCreate, RabbitUpdate


class CRUDRabbit(CRUDBase[Rabbit, RabbitCreate, RabbitUpdate]):
    pass


rabbit = CRUDRabbit(Rabbit)
