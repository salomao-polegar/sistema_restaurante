from typing import List
from datetime import datetime

class PedidoDTO():
    id: int | None = None
    status_pedido: int | None = None
    cliente: int
    datahora_recebido: datetime | None = None
    datahora_preparacao: datetime | None = None
    datahora_pronto: datetime | None = None
    datahora_finalizado: datetime | None = None
    status_pagamento: int | None = None

    def __init__(self,
    id: int | None,
    status_pedido: int | None,
    cliente: int,
    datahora_recebido: datetime | None,
    datahora_preparacao: datetime | None,
    datahora_pronto: datetime | None,
    datahora_finalizado: datetime | None,
    status_pagamento: int | None):
        
        self.id = id
        self.status_pedido = status_pedido
        self.cliente = cliente
        self.datahora_recebido = datahora_recebido
        self.datahora_preparacao = datahora_preparacao
        self.datahora_pronto = datahora_pronto
        self.datahora_finalizado = datahora_finalizado
        self.status_pagamento = status_pagamento

class ItemCheckoutDTO():
    item: int
    quantidade: int
    descricao: str
class PedidoCheckoutDTO():
    id_cliente: int
    itens: List[ItemCheckoutDTO]