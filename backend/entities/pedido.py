from pydantic import BaseModel
from datetime import datetime

class Pedido():
    id: int | None = None
    status_pedido: int | None = None
    cliente: int | None = None
    datahora_recebido: datetime | None = None
    datahora_preparacao: datetime | None = None
    datahora_pronto: datetime | None = None
    datahora_finalizado: datetime | None = None    
    status_pagamento: int | None = None
    id_pagamento: str | None = None

    def __init__(self,
            id: int | None = None,
            status_pedido: int | None = None,
            cliente: int | None = None,
            datahora_recebido: datetime | None = None,
            datahora_preparacao: datetime | None = None,
            datahora_pronto: datetime | None = None,
            datahora_finalizado: datetime | None = None,
            status_pagamento: int | None = None,
            id_pagamento: str | None = None):
        
        self.id = id
        self.status_pedido = status_pedido
        self.cliente = cliente
        self.datahora_recebido = datahora_recebido
        self.datahora_preparacao = datahora_preparacao
        self.datahora_pronto = datahora_pronto
        self.datahora_finalizado = datahora_finalizado
        self.status_pagamento = status_pagamento
        self.id_pagamento = id_pagamento

    