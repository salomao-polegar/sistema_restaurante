from pydantic import BaseModel
from datetime import datetime


class Status():
    id: int
    descricao: str
    grupos_acesso: str

class Pedido(BaseModel):
    id: int | None = None
    status_pedido: int
    cliente: str
    datahora_pedido: datetime

class ProdutoNoPedido(BaseModel):
    id_produto: int
    id_pedido: int
    