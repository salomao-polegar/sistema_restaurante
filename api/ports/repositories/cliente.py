from typing import Protocol, List

from domain.cliente import Cliente
from ports.external.database import AppDatabasePort


class ClienteRepositoryPort(Protocol):
    def __init__(self, db: AppDatabasePort):
        pass

    def insert_cliente(self, cliente: Cliente) -> Cliente:
        pass

    def get_cliente(self, cliente_id: int) -> Cliente:
        pass

    def get_todos_clientes(self) -> List[Cliente]:
        pass
    
    def edita_cliente(self, cliente: Cliente) -> Cliente:
        pass

    def delete_cliente(self, cliente: Cliente) -> bool:
        pass