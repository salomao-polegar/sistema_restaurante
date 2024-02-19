from typing import List

from domain.cliente import Cliente
from ports.repositories.cliente import ClienteRepositoryPort
from ports.services.cliente import ClienteServicePort


class ClienteNotFoundException(BaseException):
    def __init__(self, message = "Cliente não encontrado"):
        self.message = message


class ClienteAlreadyExistsException(BaseException):
    def __init__(self, message = "Cliente já existe"):
        self.message = message


class ClienteService(ClienteServicePort):
    def __init__(self, repo: ClienteRepositoryPort):
        self._repo = repo

    def inserir_cliente(self, cliente: Cliente) -> Cliente:
        _c_id = self._repo.retornar_cliente_pelo_id(cliente.id)
        _c_cpf = self._repo.retornar_cliente_pelo_cpf(cliente.cpf)
        
        if _c_id or _c_cpf:
            
            raise ClienteAlreadyExistsException()

        return self._repo.inserir_cliente(cliente)

    def retornar_cliente_pelo_id(self, cliente_id: int) -> Cliente:
        cliente = self._repo.retornar_cliente_pelo_id(cliente_id)
        if not cliente:
            raise ClienteNotFoundException()
        return cliente
    
    def retornar_cliente_pelo_cpf(self, cliente_cpf: int) -> Cliente:
        cliente = self._repo.retornar_cliente_pelo_cpf(cliente_cpf)
        if not cliente:
            raise ClienteNotFoundException()
        return cliente

    def listar_clientes(self) -> List[Cliente]:
        return self._repo.listar_clientes()
        
    def editar_cliente(self, cliente: Cliente) -> Cliente:
        _p = self._repo.retornar_cliente_pelo_id(cliente.id)

        if not _p:
            raise ClienteNotFoundException()
        
        return self._repo.editar_cliente(cliente)

    def deletar_cliente(self, cliente_id: int) -> bool:
        get_cliente = self._repo.retornar_cliente_pelo_id(cliente_id)
        if not get_cliente:
            raise ClienteNotFoundException()
        
        return self._repo.deletar_cliente(cliente_id)
