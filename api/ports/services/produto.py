# ports/produto

from typing import Protocol, List
from domain.produto import Produto
from ports.repositories.produto import ProdutoRepositoryPort


class ProdutoServicePort(Protocol):
    def __init__(self, repo: ProdutoRepositoryPort):
        pass

    def get_produto(self, produto_id: str) -> Produto:
        pass

    def get_todos_produtos(self) -> List[Produto]:
        pass

    def get_lanches(self) -> Produto:
        pass

    def get_acompanhamentos(self) -> Produto:
        pass
    
    def get_bebidas(self) -> Produto:
        pass

    def get_sobremesas(self) -> Produto:
        pass
    
    def insert_produto(self, produto: Produto) -> Produto:
        pass
    
    def edita_produto(self, produto: Produto) -> Produto:
        pass

    def delete_produto(self, produto: Produto) -> bool:
        pass
