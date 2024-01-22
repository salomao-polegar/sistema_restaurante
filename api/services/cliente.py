from typing import List

from domain.cliente import Cliente
from ports.repositories.cliente import ClienteRepositoryPort
from ports.services.cliente import ClienteServicePort


class ClienteNotFoundException(BaseException):
    pass


class ClienteAlreadyExistsException(BaseException):
    pass


class ClienteService(ClienteServicePort):
    def __init__(self, repo: ClienteRepositoryPort):
        self._repo = repo

    def insert_cliente(self, cliente: Cliente) -> Cliente:
        _p = self._repo.get_cliente(cliente.id)
        
        if _p:
            raise ClienteAlreadyExistsException()

        return self._repo.insert_cliente(cliente)

    def get_cliente(self, cliente_id: int) -> Cliente:
        cliente = self._repo.get_cliente(cliente_id)
        if not cliente:
            raise ClienteNotFoundException()
        return cliente

    def get_todos_clientes(self) -> List[Cliente]:
        return self._repo.get_todos_clientes()
        
    def edita_cliente(self, cliente: Cliente) -> Cliente:
        _p = self._repo.get_cliente(cliente.id)

        if not _p:
            raise ClienteNotFoundException()
        
        return self._repo.edita_cliente(cliente)

    def delete_cliente(self, cliente_id: int) -> bool:
        get_cliente = self._repo.get_cliente(cliente_id)
        if not get_cliente:
            raise ClienteNotFoundException()
        
        return self._repo.delete_cliente(cliente_id)
