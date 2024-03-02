from entities import Produto
from typing import Protocol, List
import json

class ProdutoAdapter:
    def produtos_to_json(dados: List[Produto] | None) -> str:
        """ Recebe uma lista de Produtos e retorna uma Lista de Dict"""
        if not dados: return {}
        if type(dados) == bool: return dados
        
        alldata = []
        
        for i in dados:
            alldata.append({
                'id' : i.id,
                'nome' : i.nome,
                'categoria' : i.categoria,
                'valor' : i.valor,
                'descricao' : i.descricao,
                'ativo' : i.ativo
                
                })
            
        return alldata