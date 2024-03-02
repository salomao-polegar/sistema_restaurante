from entities import Item
from typing import List

class ItemAdapter:
    def items_to_json(dados: List[Item] | None) -> str:
        """ Recebe uma lista de Items e retorna uma Lista de Dict"""
        if not dados: return {}
        if type(dados) == bool: return dados
        
        alldata = []
        
        for i in dados:
            alldata.append({
                'pedido' : i.pedido.id,
                'produto' : i.produto.id,
                'quantidade' : i.quantidade,
                'descricao' : i.descricao
                })
            
        return alldata