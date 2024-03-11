from common.interfaces import PagamentoInterface, MercadoPagoInterface

class MercadoPagoGateway (MercadoPagoInterface):
    repositorio: PagamentoInterface

    def __init__(self, repositorio: MercadoPagoInterface):
        self.repositorio = repositorio

    def enviar_pagamento(self, payment_data):
        retorno = self.repositorio.enviar_pagamento(payment_data)
        
        return retorno