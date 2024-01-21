from typing import List

from domain.pedido import Pedido
from ports.repositories.pedido import PedidoRepositoryPort
from ports.services.pedido import PedidoServicePort

class PedidoNotFoundException(BaseException):
    pass

class PedidoAlreadyExistsException(BaseException):
    pass


class PedidoService(PedidoServicePort):
    def __init__(self, repo: PedidoRepositoryPort):
        self._repo = repo

    def insert_pedido(self, pedido: Pedido) -> Pedido:
        if self._repo.get_pedido(pedido.id):
            raise PedidoAlreadyExistsException()        
        return self._repo.insert_pedido(pedido)
    
    def get_pedido(self, pedido_id: int) -> Pedido:
        pedido = self._repo.get_pedido(pedido_id)
        if not pedido:
            raise PedidoNotFoundException()
        return pedido

    def get_todos_pedidos(self) -> List[Pedido]:
        return self._repo.get_todos_pedidos()

    def get_pedidos_recebidos(self) -> List[Pedido]:
        return self._repo.get_pedidos_recebidos()

    def get_pedidos_em_preparacao(self) -> List[Pedido]:
        return self._repo.get_pedidos_em_preparacao()
    
    def get_pedidos_finalizados(self) -> List[Pedido]:
        return self._repo.get_pedidos_finalizados()

    def get_pedidos_nao_finalizados(self) -> List[Pedido]:
        return self._repo.get_pedidos_nao_finalizados()

    def edita_pedido(self, pedido: Pedido) -> Pedido:
        _p = self._repo.get_pedido(pedido.id)

        if not _p:
            raise PedidoNotFoundException()
        
        self._repo.edita_pedido(pedido)
        return pedido

    def delete_pedido(self, pedido: Pedido) -> bool:
        get_pedido = self._repo.get_pedido(pedido.id)
        if not get_pedido:
            raise PedidoNotFoundException()
        self._repo.delete_pedido(pedido)
        return True

    def get_fila(self) -> list:
        return self._repo.get_fila()

    def checkout(self, pedido_id: int) -> Pedido:
        pedido = self._repo.get_pedido(pedido_id)
        if not pedido:
            raise PedidoNotFoundException()
        # print(pedido)
        pedido.status_pedido = 3
        pedido = self._repo.edita_pedido(pedido)
        # print(pedido)
        return pedido