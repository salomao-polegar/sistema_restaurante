from typing import Protocol, List

from domain.pedido import Pedido
from ports.external.database import AppDatabasePort


class PedidoRepositoryPort(Protocol):
    def __init__(self, db: AppDatabasePort):
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

    def delete_pedido(self, pedido: Pedido) -> bool:
        pass
    
    def get_fila(self) -> list:
        pass

    def checkout(self, pedido_id: int) -> Pedido:
        pass