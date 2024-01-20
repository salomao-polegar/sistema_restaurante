# ports/cliente

from typing import Protocol, List
from domain.cliente import Cliente
from ports.repositories.cliente import ClienteRepositoryPort


class ClienteServicePort(Protocol):
    def __init__(self, repo: ClienteRepositoryPort):
        pass

    def insert_cliente(self, cliente: Cliente) -> Cliente:
        pass

    def get_cliente(self, cliente_id: str) -> Cliente:
        pass

    def get_todos_clientes(self) -> List[Cliente]:
        pass
        
    def edita_cliente(self, cliente: Cliente) -> Cliente:
        pass

    def delete_cliente(self, cliente: Cliente) -> bool:
        pass
