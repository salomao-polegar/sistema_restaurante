from typing import Protocol

from domain.produto import Produto
from ports.external.database import AppDatabasePort


class ProdutoRepositoryPort(Protocol):
    def __init__(self, db: AppDatabasePort):
        pass

    def get_produto(self, produto_id) -> Produto:
        pass

    def insert_produto(self, produto: Produto):
        pass

    def get_todos_produtos(self):
        pass
    
    def get_lanches(self):
        pass
    
    def get_acompanhamentos(self):
        pass
    
    def get_bebidas(self):
        pass
    
    def get_sobremesas(self):
        pass
    
    def edita_produto(self):
        pass

    def delete_produto(self, produto: Produto):
        pass