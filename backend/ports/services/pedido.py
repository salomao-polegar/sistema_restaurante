# ports/pedido

from typing import Protocol, List
from domain.pedido import Pedido
from ports.repositories.pedido import PedidoRepositoryPort


class PedidoServicePort(Protocol):
    def __init__(self, repo: PedidoRepositoryPort):
        pass

    def inserir_pedido(self, pedido: Pedido) -> Pedido:
        pass
    
    def retornar_pedido(self, pedido_id: str) -> Pedido:
        pass

    def listar_pedidos(self) -> List[Pedido]:
        pass

    def listar_pedidos_recebidos(self) -> List[Pedido]:
        pass

    def listar_pedidos_em_preparacao(self) -> List[Pedido]:
        pass
    
    def listar_pedidos_finalizados(self) -> List[Pedido]:
        pass

    def listar_pedidos_nao_finalizados(self) -> List[Pedido]:
        pass
    
    def editar_pedido(self, pedido: Pedido) -> Pedido:
        pass

    def deletar_pedido(self, pedido_id: int) -> bool:
        pass
    
    def listar_fila(self) -> list:
        pass

    def checkout(self, pedido_id: int) -> Pedido:
        pass
    
    def retorna_status_pagamento(self, pedido_id: int) -> str:
        pass
