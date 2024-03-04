from typing import Protocol, List
from entities.pedido import Pedido
from common.dto import PedidoDTO

class PedidoGatewayInterface(Protocol):
    def novo(self, pedido_dto: PedidoDTO) -> bool:
        pass
     
    def retornar_pelo_id(self, pedido_id: int) -> Pedido:
        pass
   
    def listar_todos(self) -> List[Pedido]:
        pass
    
    def editar(self, pedido_dto: PedidoDTO) -> bool:
        pass

    def deletar(self, pedido_id: int) -> bool:
        pass

    def listar_pedidos_recebidos(self) -> List[Pedido]:
        pass

    def listar_pedidos_em_preparacao(self) -> List[Pedido]:
        pass
    
    def listar_pedidos_finalizados(self) -> List[Pedido]:
        pass

    def listar_pedidos_nao_finalizados(self) -> List[Pedido]:
        pass
    
    def listar_fila(self) -> list:
        pass

    def checkout(self, pedido_id: int) -> Pedido:
        pass
        
    def retorna_status_pagamento(self, pedido_id: int) -> str:
        pass

    def retorna_ultimo_id(self) -> int:
        pass