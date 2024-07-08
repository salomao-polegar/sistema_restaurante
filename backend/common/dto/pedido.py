from typing import List, Dict
from datetime import datetime
import json

class ItemPedido():
    produto: int
    quantidade: int
    descricao: str
class PedidoDTO():
    id: int | None = None
    status_pedido: int | None = None
    cliente: int
    itens: List[ItemPedido] = []
    datahora_recebido: datetime | None = None
    datahora_preparacao: datetime | None = None
    datahora_pronto: datetime | None = None
    datahora_finalizado: datetime | None = None
    status_pagamento: int | None = None
    id_pagamento: str = None
    
    valor_total: float = 0

    def __init__(self,
    id: int | None,
    status_pedido: int | None,
    cliente: int,
    itens: List[ItemPedido]  = [],
    datahora_recebido: datetime | None = None,
    datahora_preparacao: datetime | None = None,
    datahora_pronto: datetime | None = None,
    datahora_finalizado: datetime | None = None,
    status_pagamento: int | None = None,
    id_pagamento: str = None,
    valor_total: float = None
    ):
        
        self.id = id
        self.status_pedido = status_pedido
        self.cliente = cliente
        self.itens = itens
        self.datahora_recebido = datahora_recebido
        self.datahora_preparacao = datahora_preparacao
        self.datahora_pronto = datahora_pronto
        self.datahora_finalizado = datahora_finalizado
        self.status_pagamento = status_pagamento
        self.id_pagamento = id_pagamento
        self.valor_total = valor_total

class PedidoCheckoutDTO():
    id_cliente: int
    itens: List[ItemPedido]