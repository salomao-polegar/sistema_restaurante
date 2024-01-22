from typing import Protocol, List
import domain
from ports.external.database import AppDatabasePort


class PedidoRepositoryPort(Protocol):
    def __init__(self, db: AppDatabasePort):
        pass

    def insert_pedido(self, pedido: domain.Pedido) -> domain.Pedido:
        pass
    
    def get_pedido(self, pedido_id: str) -> domain.Pedido:
        pass

    def get_todos_pedidos(self) -> List[domain.Pedido]:
        pass

    def get_pedidos_recebidos(self) -> List[domain.Pedido]:
        pass

    def get_pedidos_em_preparacao(self) -> List[domain.Pedido]:
        pass
    
    def get_pedidos_finalizados(self) -> List[domain.Pedido]:
        pass

    def get_pedidos_nao_finalizados(self) -> List[domain.Pedido]:
        pass
    
    def edita_pedido(self, pedido: domain.Pedido) -> domain.Pedido:
        pass

    def delete_pedido(self, pedido: domain.Pedido) -> bool:
        pass
    
    def get_fila(self) -> list:
        pass

    def checkout(self, pedido_id: int) -> domain.Pedido:
        pass

class ProdutoNoPedidoRepositoryPort(Protocol):
    def produtos_no_pedido(self, pedido: int) -> List[domain.ProdutoNoPedido]:
        pass

    def adicionar_produto(self, produto: domain.ProdutoNoPedido) -> domain.ProdutoNoPedido:
        pass

    def editar_produto(self, produto: domain.ProdutoNoPedido) -> domain.ProdutoNoPedido:
        pass
    