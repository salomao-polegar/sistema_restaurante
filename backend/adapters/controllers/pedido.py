from adapters.gateways import PedidoGateway, ProdutoGateway, ItemGateway, ClienteGateway, MercadoPagoGateway
from common.interfaces import DbConnection, PagamentoInterface
from common.dto import PedidoDTO, PedidoCheckoutDTO, WebhookResponseDTO
from useCases import PedidoUseCases
from adapters.presenters import PedidoAdapter
from typing import Dict, List

class PedidoController:
    def listar_todos(self, dbconnection: DbConnection) -> List[Dict]:
        
        todosOsPedidos = PedidoUseCases().listar_pedidos(
            pedido_gateway=PedidoGateway(dbconnection),
            item_gateway=ItemGateway(dbconnection),
            produto_gateway=ProdutoGateway(dbconnection)
            )
        pedidosRetorno = PedidoAdapter.pedidos_to_json(todosOsPedidos)
        # print("Pedidos Retorno", pedidosRetorno)
        return pedidosRetorno

    def listar_por_cliente_id(self, dbconnection: DbConnection, cliente_id) -> List[Dict]:
        pedidos = PedidoUseCases().listar_pedidos_por_cliente_id(
            cliente_id,
            cliente_gateway=ClienteGateway(dbconnection),
            pedido_gateway=PedidoGateway(dbconnection),
            item_gateway=ItemGateway(dbconnection),
            produto_gateway=ProdutoGateway(dbconnection)
            
        )
        return PedidoAdapter.pedidos_to_json(pedidos)
    
    # def novo(self, pedido_dto: PedidoDTO,
    #         dbconnection: DbConnection):

    #     return PedidoAdapter.pedidos_to_json(PedidoUseCases().inserir_pedido(
    #         pedido_dto, 
    #         PedidoGateway(dbconnection),
    #         ClienteGateway(dbconnection)
    #         ))
    
    def retornar_pelo_id(self, db_connection: DbConnection, pedido_id: int) -> List[Dict]:
        
        retorno_pedido = PedidoUseCases().retornar_pedido(
            pedido_id, 
            PedidoGateway(db_connection), 
            ItemGateway(db_connection),
            ProdutoGateway(db_connection)
            )
        return PedidoAdapter.pedidos_to_json([retorno_pedido])[0]
    
    
    def editar(self, db_connection: DbConnection, pedido_dto: PedidoDTO) -> Dict:
        
        return PedidoAdapter.pedidos_to_json(
            [PedidoUseCases().editar_pedido(pedido_dto, 
                                            PedidoGateway(db_connection), 
                                            ItemGateway(db_connection), 
                                            ProdutoGateway(db_connection),
                                            ClienteGateway(db_connection))
                                            ])[0]

    # def editar_status(self, db_connection: DbConnection, pedido_dto: PedidoAtualizarStatusDTO) -> Dict:
        
    #     return PedidoAdapter.pedidos_to_json(
    #         [PedidoUseCases().editar_status_pedido(pedido_dto, 
    #                                         PedidoGateway(db_connection),
    #                                         ItemGateway(db_connection), 
    #                                         ProdutoGateway(db_connection),
    #                                         )
    #                                         ])[0]

    def deletar(self, db_connection: DbConnection, pedido_id: int) -> bool:
        return PedidoUseCases().deletar_pedido(pedido_id, PedidoGateway(db_connection))

    def listar_pedidos_recebidos(self, db_connection: DbConnection) -> List[Dict]:
        
        todosOsPedidos = PedidoUseCases().listar_pedidos_recebidos(
            pedido_gateway=PedidoGateway(db_connection),
            item_gateway=ItemGateway(db_connection),
            produto_gateway=ProdutoGateway(db_connection)
        )
        return PedidoAdapter.pedidos_to_json(todosOsPedidos)

    def listar_pedidos_em_preparacao(self, db_connection: DbConnection) -> List[Dict]:
        todosOsPedidos = PedidoUseCases().listar_pedidos_em_preparacao(
            
            pedido_gateway=PedidoGateway(db_connection),
            item_gateway=ItemGateway(db_connection),
            produto_gateway=ProdutoGateway(db_connection)
        )
        return PedidoAdapter.pedidos_to_json(todosOsPedidos)
    
    def listar_pedidos_prontos(self, db_connection: DbConnection) -> List[Dict]:
        todosOsPedidos = PedidoUseCases().listar_pedidos_prontos(
            
            pedido_gateway=PedidoGateway(db_connection),
            item_gateway=ItemGateway(db_connection),
            produto_gateway=ProdutoGateway(db_connection)
        )
        return PedidoAdapter.pedidos_to_json(todosOsPedidos)
    
    def listar_pedidos_finalizados(self, db_connection: DbConnection) -> List[Dict]:
        todosOsPedidos = PedidoUseCases().listar_pedidos_finalizados(
            
            pedido_gateway=PedidoGateway(db_connection),
            item_gateway=ItemGateway(db_connection),
            produto_gateway=ProdutoGateway(db_connection)
        )
        return PedidoAdapter.pedidos_to_json(todosOsPedidos)

    # def listar_pedidos_nao_finalizados(self, db_connection: DbConnection) -> List[Dict]:
    #     todosOsPedidos = PedidoUseCases().listar_pedidos_nao_finalizados(
            
    #         pedido_gateway=PedidoGateway(db_connection),
    #         item_gateway=ItemGateway(db_connection),
    #         produto_gateway=ProdutoGateway(db_connection)
    #     )
    #     return PedidoAdapter.pedidos_to_json(todosOsPedidos)
    
    def listar_fila(self, db_connection: DbConnection) -> list:
        pedidosGateway = PedidoGateway(db_connection)
        todosOsPedidos = PedidoUseCases().listar_fila(pedidosGateway)
        return PedidoAdapter.pedidos_to_json(todosOsPedidos)

    def checkout(
            self, 
            pedido_dto: PedidoCheckoutDTO, 
            db_connection: DbConnection,
            pagamento_connection: PagamentoInterface) -> Dict:
        
        
        pedido = PedidoUseCases().checkout(pedido_dto,
            PedidoGateway(db_connection), 
            ProdutoGateway(db_connection), 
            ItemGateway(db_connection),
            ClienteGateway(db_connection),
            MercadoPagoGateway(pagamento_connection))
        
        return PedidoAdapter.pedidos_to_json([pedido])[0]
        
    def retorna_status_pagamento(self, pedido_id: int, db_connection: DbConnection) -> str:
        
        pedidosGateway = PedidoGateway(db_connection)
        
        return PedidoUseCases().retorna_status_pagamento(pedido_id, pedidosGateway)

    def atualiza_status_pagamento(self, status: WebhookResponseDTO, db_connection: DbConnection) -> PedidoDTO:
        
        return PedidoUseCases().atualiza_status_pagamento(status, 
                                                          PedidoGateway(db_connection),
                                                          ItemGateway(db_connection),
                                                          ProdutoGateway(db_connection),
                                                          ClienteGateway(db_connection))
