from typing import Protocol, List
from entities.cliente import Cliente
from common.dto import ClienteDTO

class ClienteGatewayInterface(Protocol):
    def novo(self, cliente_dto: ClienteDTO) -> Cliente:
        pass

    def retornar_pelo_id(self, cliente_id: int) -> Cliente:
        pass
    
    def retornar_pelo_cpf(self, cliente_cpf: str) -> Cliente:
        pass

    def retornar_pelo_email(self, cliente_cpf: str) -> Cliente:
        pass

    def listar_todos(self) -> List[Cliente]:
        pass
    
    def editar(self, cliente_dto: ClienteDTO) -> Cliente:
        pass

    def deletar(self, cliente_id: int) -> Cliente:
        pass

