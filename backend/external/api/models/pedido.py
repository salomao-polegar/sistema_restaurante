from datetime import datetime
from typing import List
from pydantic import BaseModel


class ItemCheckoutModel(BaseModel):
    produto: int
    quantidade: int
    
    descricao: str | None = None

class PedidoBaseModel(BaseModel):
    id: int | None = None
    status_pedido: int | None = None
    
    itens: List[ItemCheckoutModel] | None = None
    datahora_recebido: datetime | None = None
    datahora_preparacao: datetime | None = None
    datahora_pronto: datetime | None = None
    datahora_finalizado: datetime | None = None
    status_pagamento: int | None = None
    id_pagamento: str | None = None
    valor_total: float = 0

class PedidoModel(PedidoBaseModel):
    cliente: int

class PedidoEditarModel(PedidoBaseModel):
    cliente: int | None = None

class ItemModel(BaseModel):
    produto: int
    pedido: int
    quantidade: int = 0
    descricao: str | None
    valor: float
    
    
class PedidoCheckoutModel(BaseModel):
    id_cliente: int
    itens: List[ItemCheckoutModel]

# class PedidoAtualizarStatusModel(BaseModel):
#     id: int
#     status_pedido: int