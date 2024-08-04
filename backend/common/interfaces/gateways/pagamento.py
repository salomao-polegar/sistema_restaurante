from typing import Protocol, Dict
from common.dto import PagamentoDTO

class PagamentoInterface(Protocol):
    
    def enviar_pagamento(self, payment_data: PagamentoDTO) -> Dict:
        pass