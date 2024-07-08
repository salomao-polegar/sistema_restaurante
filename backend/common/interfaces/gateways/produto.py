from typing import Protocol, List
from entities.produto import Produto
from common.dto import ProdutoDTO

class ProdutoGatewayInterface(Protocol):
    def novo(self, produto_dto: ProdutoDTO) -> Produto:
        pass
     
    def retornar_pelo_id(self, produto_id: int) -> Produto:
        pass
   
    def listar_todos(self) -> List[Produto]:
        pass
    
    def editar(self, produto_dto: ProdutoDTO) -> Produto:
        pass

    def deletar(self, produto_id: int) -> bool:
        pass

    def listar_lanches(self) -> List[Produto]:
        pass
    
    def listar_acompanhamentos(self) -> List[Produto]:
        pass
    
    def listar_bebidas(self) -> List[Produto]:
        pass
    
    def listar_sobremesas(self) -> List[Produto]:
        pass