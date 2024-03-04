from adapters.gateways import PedidoGateway, ProdutoGateway, ItemGateway, ClienteGateway
from common.interfaces import DbConnection
from common.dto import PedidoDTO, PedidoCheckoutDTO
from useCases import PedidoUseCases
from adapters.presenters import PedidoAdapter
from typing import Dict, List

class PedidoController:
    def listar_todos(self, dbconnection: DbConnection) -> List[Dict]:
        pedidosGateway = PedidoGateway(dbconnection)
        todosOsPedidos = PedidoUseCases().listar_pedidos(pedidosGateway)
        return PedidoAdapter.pedidos_to_json(todosOsPedidos)
    
    def novo(self, pedido_dto: PedidoDTO,
            dbconnection: DbConnection):

        return PedidoAdapter.pedidos_to_json(PedidoUseCases().inserir_pedido(pedido_dto, PedidoGateway(dbconnection)))
    
    def retornar_pelo_id(self, db_connection: DbConnection, pedido_id: int) -> List[Dict]:
        pedidoGateway = PedidoGateway(db_connection)
        retorno_pedido = PedidoUseCases().retornar_pedido(pedido_id, pedidoGateway)
        return PedidoAdapter.pedidos_to_json([retorno_pedido])
    
    
    def editar(self, db_connection: DbConnection, pedido_dto: PedidoDTO) -> bool:
        
        return PedidoUseCases().editar_pedido(pedido_dto, PedidoGateway(db_connection))

    def deletar(self, db_connection: DbConnection, pedido_id: int) -> bool:
        return PedidoUseCases().deletar_pedido(pedido_id, PedidoGateway(db_connection))

    def listar_pedidos_recebidos(self, db_connection: DbConnection) -> List[Dict]:
        pedidosGateway = PedidoGateway(db_connection)
        todosOsPedidos = PedidoUseCases().listar_pedidos_recebidos(pedidosGateway)
        return PedidoAdapter.pedidos_to_json(todosOsPedidos)

    def listar_pedidos_em_preparacao(self, db_connection: DbConnection) -> List[Dict]:
        pedidosGateway = PedidoGateway(db_connection)
        todosOsPedidos = PedidoUseCases().listar_pedidos_em_preparacao(pedidosGateway)
        return PedidoAdapter.pedidos_to_json(todosOsPedidos)
    
    def listar_pedidos_finalizados(self, db_connection: DbConnection) -> List[Dict]:
        pedidosGateway = PedidoGateway(db_connection)
        todosOsPedidos = PedidoUseCases().listar_pedidos_finalizados(pedidosGateway)
        return PedidoAdapter.pedidos_to_json(todosOsPedidos)

    def listar_pedidos_nao_finalizados(self, db_connection: DbConnection) -> List[Dict]:
        pedidosGateway = PedidoGateway(db_connection)
        todosOsPedidos = PedidoUseCases().listar_pedidos_nao_finalizados(pedidosGateway)
        return PedidoAdapter.pedidos_to_json(todosOsPedidos)
    
    def listar_fila(self, db_connection: DbConnection) -> list:
        pedidosGateway = PedidoGateway(db_connection)
        todosOsPedidos = PedidoUseCases().listar_fila(pedidosGateway)
        return PedidoAdapter.pedidos_to_json(todosOsPedidos)

    def checkout(self, pedido_dto: PedidoCheckoutDTO, db_connection: DbConnection) -> bool:
        pedido = PedidoUseCases().checkout(pedido_dto,
            PedidoGateway(db_connection), 
            ProdutoGateway(db_connection), 
            ItemGateway(db_connection),
            ClienteGateway(db_connection))
        
        return PedidoAdapter.pedidos_to_json([pedido])
        
    def retorna_status_pagamento(self, pedido_id: int, db_connection: DbConnection) -> str:
        
        pedidosGateway = PedidoGateway(db_connection)
        
        return PedidoUseCases().retorna_status_pagamento(pedido_id, pedidosGateway)
