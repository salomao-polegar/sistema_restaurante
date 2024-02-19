from typing import List
import domain
from ports.repositories.pedido import PedidoRepositoryPort
from ports.services.pedido import PedidoServicePort

class PedidoNotFoundException(BaseException):
    def __init__(self, message = "Pedido não encontrado"):
        self.message = message


class PedidoAlreadyExistsException(BaseException):
    def __init__(self, message = "Pedido já existe"):
        self.message = message

class PedidoService(PedidoServicePort):
    def __init__(self, repo: PedidoRepositoryPort):
        self._repo = repo

    def inserir_pedido(self, pedido: domain.Pedido) -> domain.Pedido:
        if self._repo.retornar_pedido(pedido.id):
            raise PedidoAlreadyExistsException()        
        return self._repo.inserir_pedido(pedido)
    
    def retornar_pedido(self, pedido_id: int) -> domain.Pedido:
        pedido = self._repo.retornar_pedido(pedido_id)
        if not pedido:
            raise PedidoNotFoundException()
        return pedido

    def listar_pedidos(self) -> List[domain.Pedido]:
        return self._repo.listar_pedidos()

    def listar_pedidos_recebidos(self) -> List[domain.Pedido]:
        return self._repo.listar_pedidos_recebidos()

    def listar_pedidos_em_preparacao(self) -> List[domain.Pedido]:
        return self._repo.listar_pedidos_em_preparacao()
    
    def listar_pedidos_finalizados(self) -> List[domain.Pedido]:
        return self._repo.listar_pedidos_finalizados()

    def listar_pedidos_nao_finalizados(self) -> List[domain.Pedido]:
        return self._repo.listar_pedidos_nao_finalizados()

    def editar_pedido(self, pedido: domain.Pedido) -> domain.Pedido:
        _p = self._repo.retornar_pedido(pedido.id)

        if not _p:
            raise PedidoNotFoundException()
        return self._repo.editar_pedido(pedido)

    def deletar_pedido(self, pedido_id: int) -> bool:
        get_pedido = self._repo.retornar_pedido(pedido_id)
        if not get_pedido:
            raise PedidoNotFoundException()
        
        return self._repo.deletar_pedido(pedido_id)

    def listar_fila(self) -> list:
        return self._repo.listar_fila()

    def checkout(self, pedido_id: int) -> domain.Pedido:
        pedido = self._repo.retornar_pedido(pedido_id)
        if not pedido:
            raise PedidoNotFoundException()

        pedido.status_pedido = 3

        return self._repo.editar_pedido(pedido)
    
        
    def retorna_status_pagamento(self, pedido_id: int) -> str:
        pedido = self._repo.retornar_pedido(pedido_id)
        if not pedido:
            raise PedidoNotFoundException()
        
        return self._repo.retorna_status_pagamento(pedido_id)

