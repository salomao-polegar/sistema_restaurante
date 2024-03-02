from pydantic import BaseModel
from datetime import datetime

class Pedido(BaseModel):
    id: int | None = None
    status_pedido: int | None = None
    cliente: int | None = None
    datahora_recebido: datetime | None = None
    datahora_preparacao: datetime | None = None
    datahora_pronto: datetime | None = None
    datahora_finalizado: datetime | None = None
    
    status_pagamento: int | None = None


    