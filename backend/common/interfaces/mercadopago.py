from typing import Protocol
from typing import Dict
from common.dto import PagamentoDTO

class MercadoPagoInterface(Protocol):

    def enviar_pagamento(self, payment_data: PagamentoDTO) -> Dict:
        pass
