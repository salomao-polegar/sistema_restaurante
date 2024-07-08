from datetime import datetime
from typing import List
from pydantic import BaseModel


class ItemCheckoutModel(BaseModel):
    produto: int
    quantidade: int
    valor: float
    descricao: str | None = None
class PedidoModel(BaseModel):
    id: int | None = None
    status_pedido: int | None = None
    cliente: int
    itens: List[ItemCheckoutModel] | None = None
    datahora_recebido: datetime | None = None
    datahora_preparacao: datetime | None = None
    datahora_pronto: datetime | None = None
    datahora_finalizado: datetime | None = None
    status_pagamento: int | None = None
    id_pagamento: str | None = None
    valor_total: float = 0


class ItemModel(BaseModel):
    produto: int
    pedido: int
    quantidade: int = 0
    descricao: str | None
    valor: float
    
    
class PedidoCheckoutModel(BaseModel):
    id_cliente: int
    itens: List[ItemCheckoutModel]