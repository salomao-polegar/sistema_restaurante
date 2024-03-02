from adapters.gateways import ClienteGateway
from common.interfaces import DbConnection
from common.dto import ClienteDTO
from useCases import ClienteUseCases
from adapters.presenters import ClienteAdapter
from typing import Dict, List

class ClienteController:
    def listar_todos(self, dbconnection: DbConnection) -> List[Dict]:
        clientesGateway = ClienteGateway(dbconnection)
        todosOsClientes = ClienteUseCases().listar_clientes(clientesGateway)
        return ClienteAdapter.clientes_to_json(todosOsClientes)
        
    def novo(self, cliente_dto: ClienteDTO,
            dbconnection: DbConnection):

        return ClienteAdapter.clientes_to_json(ClienteUseCases().inserir_cliente(cliente_dto, ClienteGateway(dbconnection)))
    
    def retornar_pelo_id(self, db_connection: DbConnection, cliente_id: int) -> List[Dict]:
        clienteGateway = ClienteGateway(db_connection)
        retorno_cliente = ClienteUseCases().retornar_pelo_id(cliente_id, clienteGateway)
        return ClienteAdapter.clientes_to_json([retorno_cliente])
    
    def retornar_pelo_cpf(self, db_connection: DbConnection, cliente_cpf: int) -> List[Dict]:
        clienteGateway = ClienteGateway(db_connection)
        retorno_cliente = ClienteUseCases().retornar_pelo_cpf(cliente_cpf, clienteGateway)
        return ClienteAdapter.clientes_to_json([retorno_cliente])
    
    def editar(self, db_connection: DbConnection, cliente_dto: ClienteDTO) -> bool:
        
        return ClienteUseCases().editar_cliente(cliente_dto, ClienteGateway(db_connection))

    def deletar(self, db_connection: DbConnection, cliente_id: int) -> bool:
        return ClienteUseCases().deletar_cliente(cliente_id, ClienteGateway(db_connection))
