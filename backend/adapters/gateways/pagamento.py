from common.interfaces import PagamentoInterface, MercadoPagoInterface
from common.dto import PagamentoDTO

class PagamentoGateway (PagamentoInterface):
    repositorio: MercadoPagoInterface

    def __init__(self, repositorio: MercadoPagoInterface):
        self.repositorio = repositorio

    def enviar_pagamento(self, payment_data: PagamentoDTO):
        retorno = self.repositorio.enviar_pagamento(payment_data)
        
        return retorno