from typing import Protocol

class PagamentoInterface(Protocol):
    
    def enviar_pagamento(self, payment_data):
        pass