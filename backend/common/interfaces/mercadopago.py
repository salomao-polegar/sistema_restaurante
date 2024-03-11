from typing import Protocol

class MercadoPagoInterface(Protocol):

    def enviar_pagamento(self, payment_data):
        pass
