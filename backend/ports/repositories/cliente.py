from typing import Protocol, List

from domain.cliente import Cliente
from ports.external.database import AppDatabasePort

class ClienteRepositoryPort(Protocol):
    def __init__(self, db: AppDatabasePort):
        pass

    def inserir_cliente(self, cliente: Cliente) -> Cliente:
        pass

    def retornar_cliente_pelo_id(self, cliente_id: int) -> Cliente:
        pass
    
    def retornar_cliente_pelo_cpf(self, cliente_cpf: str) -> Cliente:
        pass

    def listar_clientes(self) -> List[Cliente]:
        pass
    
    def editar_cliente(self, cliente: Cliente) -> Cliente:
        pass

    def deletar_cliente(self, cliente_id: int) -> bool:
        pass