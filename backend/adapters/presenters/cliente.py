from entities import Cliente
from typing import Dict, List
import json

class ClienteAdapter:
    def clientes_to_json(dados: List[Cliente] | None) -> List[Dict]:
        """ Recebe uma lista de Clientes e retorna uma Lista de Dict"""
        if not dados: return {}
        if type(dados) == bool: return dados
        
        alldata = []
        
        for i in dados:
            
            alldata.append({
                'id': i.id, 
                'cpf': i.cpf,
                'nome': i.nome,
                'email': i.email,
                'hashed_password': i.hashed_password,
                'telefone': i.telefone,
                'ativo': i.ativo,
                })
            
        return alldata