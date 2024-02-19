from typing import Protocol, List
import domain
from ports.external.database import AppDatabasePort


class PedidoRepositoryPort(Protocol):
    def __init__(self, db: AppDatabasePort):
        pass

    def inserir_pedido(self, pedido: domain.Pedido) -> domain.Pedido:
        pass
    
    def retornar_pedido(self, pedido_id: str) -> domain.Pedido:
        pass

    def listar_pedidos(self) -> List[domain.Pedido]:
        pass

    def listar_pedidos_recebidos(self) -> List[domain.Pedido]:
        pass

    def listar_pedidos_em_preparacao(self) -> List[domain.Pedido]:
        pass
    
    def listar_pedidos_finalizados(self) -> List[domain.Pedido]:
        pass

    def listar_pedidos_nao_finalizados(self) -> List[domain.Pedido]:
        pass
    
    def editar_pedido(self, pedido: domain.Pedido) -> domain.Pedido:
        pass

    def deletar_pedido(self, pedido_id: int) -> bool:
        pass
    
    def listar_fila(self) -> list:
        pass

    def checkout(self, pedido_id: int) -> domain.Pedido:
        pass
    
    def retorna_status_pagamento(self, pedido_id: int) -> str:
        pass

    