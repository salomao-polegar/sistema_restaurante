from typing import Protocol, List

from domain.produto import Produto
from ports.external.database import AppDatabasePort


class ProdutoRepositoryPort(Protocol):
    def __init__(self, db: AppDatabasePort):
        pass

    def get_produto(self, produto_id: int) -> Produto:
        pass

    def insert_produto(self, produto: Produto) -> Produto:
        pass

    def get_todos_produtos(self) -> List[Produto]:
        pass
    
    def get_lanches(self) -> List[Produto]:
        pass
    
    def get_acompanhamentos(self) -> List[Produto]:
        pass
    
    def get_bebidas(self) -> List[Produto]:
        pass
    
    def get_sobremesas(self) -> List[Produto]:
        pass
    
    def edita_produto(self, produto: Produto) -> List[Produto]:
        pass

    def delete_produto(self, produto: Produto) -> bool:
        pass