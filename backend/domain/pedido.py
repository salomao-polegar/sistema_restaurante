from pydantic import BaseModel
from datetime import datetime

class Pedido(BaseModel):
    id: int | None = None
    status_pedido: int | None = None
    cliente: int
    datahora: datetime | None = None
    status_pagamento_pedido: int | None = None


    