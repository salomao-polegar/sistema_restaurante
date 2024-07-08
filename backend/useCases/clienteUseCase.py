from entities import Cliente
from common.exceptions import ClienteNotFoundException, ClienteAlreadyExistsException
from common.interfaces.gateways import ClienteGatewayInterface
from typing import List
from common.dto import ClienteDTO

class ClienteUseCases ():
    def inserir_cliente(self,
        cliente_dto: ClienteDTO,
        cliente_gateway: ClienteGatewayInterface) -> Cliente:

        if cliente_dto.cpf: 
            cliente = cliente_gateway.retornar_pelo_cpf(cliente_dto.cpf)
            if cliente: raise ClienteAlreadyExistsException()
        
        if cliente_dto.email: 
            cliente = cliente_gateway.retornar_pelo_email(cliente_dto.email)
            if cliente: raise ClienteAlreadyExistsException(message="E-mail já cadastrado")

        novo_cliente = Cliente(
            id = None, 
            cpf = cliente_dto.cpf, 
            nome = cliente_dto.nome, 
            email = cliente_dto.email, 
            hashed_password = cliente_dto.hashed_password,
            telefone = cliente_dto.telefone, 
            ativo = cliente_dto.ativo) 
        
        
        return cliente_gateway.novo(novo_cliente)
    
    def listar_clientes(self, cliente_gateway: ClienteGatewayInterface) -> List[Cliente]:
        return cliente_gateway.listar_todos()
        
    def retornar_pelo_id(self, cliente_id: int, cliente_gateway: ClienteGatewayInterface) -> Cliente:
        cliente: Cliente = cliente_gateway.retornar_pelo_id(cliente_id)
        if not cliente: raise ClienteNotFoundException()
        return cliente
    
    def retornar_pelo_cpf(self, cliente_cpf: str, cliente_gateway: ClienteGatewayInterface) -> Cliente:
        cliente: Cliente = cliente_gateway.retornar_pelo_cpf(cliente_cpf)
        if not cliente: raise ClienteNotFoundException()
        return cliente

    
    def editar_cliente(self,
            cliente_dto: ClienteDTO,
            cliente_gateway: ClienteGatewayInterface) -> Cliente:
        if not cliente_dto.id: raise ClienteNotFoundException

        cliente = cliente_gateway.retornar_pelo_id(cliente_dto.id)
        if not cliente: ClienteNotFoundException()
        cliente_editar = Cliente(
            id = cliente_dto.id, 
            cpf = cliente_dto.cpf, 
            nome = cliente_dto.nome, 
            email = cliente_dto.email, 
            hashed_password = cliente_dto.hashed_password,
            telefone = cliente_dto.telefone, 
            ativo = cliente_dto.ativo) 
        
        return cliente_gateway.editar(cliente_editar)

    def deletar_cliente(self, cliente_id: int, cliente_gateway: ClienteGatewayInterface) -> bool:
        if not cliente_gateway.retornar_pelo_id(cliente_id): raise ClienteNotFoundException()
        return cliente_gateway.deletar(cliente_id)

