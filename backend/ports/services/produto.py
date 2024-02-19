# ports/produto

from typing import Protocol, List
from domain.produto import Produto
from ports.repositories.produto import ProdutoRepositoryPort


class ProdutoServicePort(Protocol):
    def __init__(self, repo: ProdutoRepositoryPort):
        pass

    def inserir_produto(self, produto: Produto) -> Produto:
        pass
    
    def retornar_produto(self, produto_id: str) -> Produto:
        pass

    def listar_produtos(self) -> List[Produto]:
        pass

    def listar_lanches(self) -> Produto:
        pass

    def listar_acompanhamentos(self) -> Produto:
        pass
    
    def listar_bebidas(self) -> Produto:
        pass

    def listar_sobremesas(self) -> Produto:
        pass
    
    def editar_produto(self, produto: Produto) -> Produto:
        pass

    def deletar_produto(self, produto_id: int) -> bool:
        pass
