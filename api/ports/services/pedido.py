# ports/pedido

from typing import Protocol, List
from domain.pedido import Pedido
import domain
from ports.repositories.pedido import PedidoRepositoryPort


class PedidoServicePort(Protocol):
    def __init__(self, repo: PedidoRepositoryPort):
        pass

    def insert_pedido(self, pedido: Pedido) -> Pedido:
        pass
    
    def get_pedido(self, pedido_id: str) -> Pedido:
        pass

    def get_todos_pedidos(self) -> List[Pedido]:
        pass

    def get_pedidos_recebidos(self) -> List[Pedido]:
        pass

    def get_pedidos_em_preparacao(self) -> List[Pedido]:
        pass
    
    def get_pedidos_finalizados(self) -> List[Pedido]:
        pass

    def get_pedidos_nao_finalizados(self) -> List[Pedido]:
        pass
    
    def edita_pedido(self, pedido: Pedido) -> Pedido:
        pass

    def delete_pedido(self, pedido_id: int) -> bool:
        pass
    
    def get_fila(self) -> list:
        pass

    def checkout(self, pedido_id: int) -> Pedido:
        pass

class ProdutoNoPedidoServicePort(Protocol):
    def produtos_no_pedido(self, pedido: int) -> List[domain.ProdutoNoPedido]:
        pass
    
    def adicionar_produto(self, produto: domain.ProdutoNoPedido) -> domain.ProdutoNoPedido:
        pass

    def editar_produto(self, produto: domain.ProdutoNoPedido) -> domain.ProdutoNoPedido:
        pass        

    def remover_produto(self, produto: domain.ProdutoNoPedido) -> bool:
        pass