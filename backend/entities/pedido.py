from typing import List
from datetime import datetime

class ItemPedido():
    produto: str | None = None
    quantidade: int | None = None
    descricao: str | None = None
    valor: float

    def __init__(self,
                produto: str | None,
                quantidade: int | None,
                descricao: str | None,
                valor: float):

        self.produto = produto
        self.quantidade = quantidade
        self.descricao = descricao
        self.valor = valor
class Pedido():
    id: int | None = None
    status_pedido: int | None = None
    cliente: int | None = None
    itens: List[ItemPedido] | None = None
    datahora_recebido: datetime | None = None
    datahora_preparacao: datetime | None = None
    datahora_pronto: datetime | None = None
    datahora_finalizado: datetime | None = None    
    status_pagamento: int | None = None
    id_pagamento: str | None = None
    valor_total: float

    def __init__(self,
            id: int | None = None,
            status_pedido: int | None = None,
            cliente: int | None = None,
            itens: List[ItemPedido] = [],
            datahora_recebido: datetime | None = None,
            datahora_preparacao: datetime | None = None,
            datahora_pronto: datetime | None = None,
            datahora_finalizado: datetime | None = None,
            status_pagamento: int | None = None,
            id_pagamento: str | None = None,
            valor_total: float = 0):
        
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

    