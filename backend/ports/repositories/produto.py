from typing import Protocol, List

from domain.produto import Produto
from ports.external.database import AppDatabasePort


class ProdutoRepositoryPort(Protocol):
    def __init__(self, db: AppDatabasePort):
        pass

    def inserir_produto(self, produto: Produto) -> Produto:
        pass

    def retornar_produto(self, produto_id: int) -> Produto:
        pass

    def listar_produtos(self) -> List[Produto]:
        pass
    
    def listar_lanches(self) -> List[Produto]:
        pass
    
    def listar_acompanhamentos(self) -> List[Produto]:
        pass
    
    def listar_bebidas(self) -> List[Produto]:
        pass
    
    def listar_sobremesas(self) -> List[Produto]:
        pass
    
    def editar_produto(self, produto: Produto) -> Produto:
        pass

    def deletar_produto(self, produto_id: int) -> bool:
        pass