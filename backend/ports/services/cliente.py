# ports/cliente

from typing import Protocol, List
from domain.cliente import Cliente
from ports.repositories.cliente import ClienteRepositoryPort


class ClienteServicePort(Protocol):
    def __init__(self, repo: ClienteRepositoryPort):
        pass

    def inserir_cliente(self, cliente: Cliente) -> Cliente:
        pass

    def retornar_cliente_pelo_id(self, cliente_id: int = None) -> Cliente:
        pass

    def retornar_cliente_pelo_cpf(self, cliente_cpf: str) -> Cliente:
        pass

    def listar_clientes(self) -> List[Cliente]:
        pass
        
    def editar_cliente(self, cliente: Cliente) -> Cliente:
        pass

    def deletar_cliente(self, cliente_id: int) -> bool:
        pass
