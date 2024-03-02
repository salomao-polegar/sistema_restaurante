from entities import Pedido
from typing import Protocol, List
import json

class PedidoAdapter:
    def pedidos_to_json(dados: List[Pedido] | None) -> str:
        """ Recebe uma lista de Pedidos e retorna uma Lista de Dict"""
        if not dados: return {}
        if type(dados) == bool: return dados
        
        alldata = []
        
        for i in dados:
            alldata.append({
                'id' : i.id,
                'status_pedido' : i.status_pedido,
                'cliente' : i.cliente,
                'datahora' : i.datahora_recebido,
                'datahora_recebido': i.datahora_recebido,
                "datahora_preparacao": i.datahora_preparacao,
                "datahora_pronto": i.datahora_pronto,
                "datahora_finalizado": i.datahora_finalizado,

                'status_pagamento' : i.status_pagamento})
            
        return alldata