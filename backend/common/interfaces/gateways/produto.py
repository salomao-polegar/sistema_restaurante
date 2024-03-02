from typing import Protocol, List
from entities.produto import Produto
from common.dto import ProdutoDTO

class ProdutoGatewayInterface(Protocol):
    def novo(self, cliente_dto: ProdutoDTO) -> bool:
        pass
     
    def retornar_pelo_id(self, cliente_id: int) -> Produto:
        pass
   
    def listar_todos(self) -> List[Produto]:
        pass
    
    def editar(self, cliente_dto: ProdutoDTO) -> bool:
        pass

    def deletar(self, cliente_id: int) -> bool:
        pass

    def listar_lanches(self) -> List[Produto]:
        pass
    
    def listar_acompanhamentos(self) -> List[Produto]:
        pass
    
    def listar_bebidas(self) -> List[Produto]:
        pass
    
    def listar_sobremesas(self) -> List[Produto]:
        pass