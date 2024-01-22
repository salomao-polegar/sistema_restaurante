from pydantic import BaseModel
from datetime import datetime

class Pedido(BaseModel):
    id: int | None
    status_pedido: int | None = None
    cliente: int | None = None
    datahora: datetime | None = None

class ProdutoNoPedido(BaseModel):
    produto: int
    pedido: int
    quantidade: int
    