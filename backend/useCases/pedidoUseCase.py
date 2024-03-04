from entities import Pedido, Produto, Cliente, Item
from common.exceptions import PedidoNotFoundException, ProdutoNotFoundException, ClienteNotFoundException
from common.interfaces.gateways import PedidoGatewayInterface, ProdutoGatewayInterface, ItemGatewayInterface, ClienteGatewayInterface
from common.dto import PedidoCheckoutDTO
from typing import List


class PedidoUseCases ():
    def inserir_pedido(self, 
        pedido_dto: Pedido,
        pedido_gateway: PedidoGatewayInterface) -> bool:
        
        # produto_inserir = Pedido(
        #     status_pedido = pedido_dto.status_pedido,
        #     cliente=pedido_dto.cliente,
        #     datahora_recebido=pedido_dto.datahora_recebido,
        #     datahora_preparacao= pedido_dto.datahora_preparacao,
        #     datahora_pronto= pedido_dto.datahora_pronto,
        #     datahora_finalizado= pedido_dto.datahora_finalizado,
        #     status_pagamento_pedido=pedido_dto.status_pagamento_pedido)
         
        pedido_gateway.novo(pedido_dto)
        return True      
    
    def retornar_pedido(self, pedido_id: int, pedido_gateway: PedidoGatewayInterface) -> Pedido:
        pedido = pedido_gateway.retornar_pelo_id(pedido_id)
        if not pedido:
            raise PedidoNotFoundException()
        return pedido

    def listar_pedidos(self, pedido_gateway: PedidoGatewayInterface) -> List[Pedido]:
        return pedido_gateway.listar_todos()

    def listar_pedidos_recebidos(self, pedido_gateway: PedidoGatewayInterface) -> List[Pedido]:
        return pedido_gateway.listar_pedidos_recebidos()

    def listar_pedidos_em_preparacao(self, pedido_gateway: PedidoGatewayInterface) -> List[Pedido]:
        return pedido_gateway.listar_pedidos_em_preparacao()
    
    def listar_pedidos_finalizados(self, pedido_gateway: PedidoGatewayInterface) -> List[Pedido]:
        return pedido_gateway.listar_pedidos_finalizados()

    def listar_pedidos_nao_finalizados(self, pedido_gateway: PedidoGatewayInterface) -> List[Pedido]:
        return pedido_gateway.listar_pedidos_nao_finalizados()

    def editar_pedido(self, pedido: Pedido, pedido_gateway: PedidoGatewayInterface) -> bool:
        _p = pedido_gateway.retornar_pelo_id(pedido.id)

        if not _p:
            raise PedidoNotFoundException()
        return pedido_gateway.editar(pedido)

    def deletar_pedido(self, pedido_id: int, pedido_gateway: PedidoGatewayInterface) -> bool:
        get_pedido = pedido_gateway.retornar_pelo_id(pedido_id)
        if not get_pedido:
            raise PedidoNotFoundException()
        
        return pedido_gateway.deletar(pedido_id)

    def listar_fila(self, pedido_gateway: PedidoGatewayInterface) -> list:
        return pedido_gateway.listar_fila()

    def checkout(
            self, 
            produtos_checkout: PedidoCheckoutDTO,
            pedido_gateway: PedidoGatewayInterface, 
            produto_gateway: ProdutoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            cliente_gateway: ClienteGatewayInterface) -> Pedido:
        # TODO
        # Recebe uma lista com produtos e retorna o pedido criado
        for produto in produtos_checkout.itens:
            prod = produto_gateway.retornar_pelo_id(produto.item)
            if not prod:
                raise ProdutoNotFoundException()
        
        if not cliente_gateway.retornar_pelo_id(produtos_checkout.id_cliente):
            raise ClienteNotFoundException()
        
        pedido_gateway.novo(Pedido(cliente=produtos_checkout.id_cliente))

        pedido = pedido_gateway.retornar_pelo_id(pedido_gateway.retorna_ultimo_id())

        for produto in produtos_checkout.itens:
            item_gateway.novo(Item(produto=Produto(id=produto.item), pedido=pedido, quantidade = produto.quantidade, descricao=produto.descricao))
        
        return pedido
    
        
    def retorna_status_pagamento(self, pedido_id: int, pedido_gateway: PedidoGatewayInterface) -> str:
        pedido = pedido_gateway.retornar_pelo_id(pedido_id)
        if not pedido:
            raise PedidoNotFoundException()
        
        return pedido_gateway.retorna_status_pagamento(pedido_id)
