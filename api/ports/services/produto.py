# ports/produto

from typing import Protocol
from domain.produto import Produto
from ports.repositories.produto import ProdutoRepositoryPort


class ProdutoServicePort(Protocol):
    def __init__(self, repo: ProdutoRepositoryPort):
        pass

    def get_produto(self, produto_id: str):
        pass

    def insert_produto(self, produto: Produto):
        pass
    
    def edita_produto(self, produto: Produto):
        pass

    def get_todos_produtos(self):
        pass

    def delete_produto(self, produto: Produto):
        pass
