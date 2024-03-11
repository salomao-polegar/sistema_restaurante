from entities import Pedido, Produto, Cliente, Item
from common.exceptions import PedidoNotFoundException, ProdutoNotFoundException, ClienteNotFoundException
from common.interfaces.gateways import PedidoGatewayInterface, ProdutoGatewayInterface, ItemGatewayInterface, ClienteGatewayInterface, PagamentoInterface   
from common.dto import PedidoCheckoutDTO, WebhookResponseDTO, ItemDTO, PedidoDTO
from typing import List
import pandas as pd

class PedidoUseCases ():
    def inserir_pedido(self, 
        pedido_dto: Pedido,
        pedido_gateway: PedidoGatewayInterface) -> bool:         
        pedido_gateway.novo(pedido_dto)
        return True      
    
    def retornar_pedido(
            self, 
            pedido_id: int, 
            pedido_gateway: PedidoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            produto_gateway: ProdutoGatewayInterface
            ) -> PedidoDTO:
        
        return self.ajustar_pedidos_retorno(
            [pedido_gateway.retornar_pelo_id(pedido_id)],
            pedido_gateway,
            produto_gateway,
            item_gateway
        )[0]

    def listar_pedidos(
            self, 
            pedido_gateway: PedidoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            produto_gateway: ProdutoGatewayInterface) -> List[Pedido]:

        return self.ajustar_pedidos_retorno(
            pedido_gateway.listar_todos(),
            pedido_gateway,
            produto_gateway,
            item_gateway
        )

    def listar_pedidos_recebidos(self, 
            pedido_gateway: PedidoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            produto_gateway: ProdutoGatewayInterface) -> List[Pedido]:
        
        return self.ajustar_pedidos_retorno(
            pedido_gateway.listar_pedidos_recebidos(),
            pedido_gateway,
            produto_gateway,
            item_gateway)

    def listar_pedidos_em_preparacao(
            self, 
            pedido_gateway: PedidoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            produto_gateway: ProdutoGatewayInterface) -> List[Pedido]:
        
        return self.ajustar_pedidos_retorno(
            pedido_gateway.listar_pedidos_em_preparacao(),
            pedido_gateway,
            produto_gateway,
            item_gateway)
    
    def listar_pedidos_finalizados(self, 
            pedido_gateway: PedidoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            produto_gateway: ProdutoGatewayInterface) -> List[Pedido]:
        
        return self.ajustar_pedidos_retorno(
            pedido_gateway.listar_pedidos_finalizados(),
            pedido_gateway,
            produto_gateway,
            item_gateway)

    def listar_pedidos_nao_finalizados(self, 
            pedido_gateway: PedidoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            produto_gateway: ProdutoGatewayInterface) -> List[Pedido]:
        
        return self.ajustar_pedidos_retorno(
            pedido_gateway.listar_pedidos_nao_finalizados(),
            pedido_gateway,
            produto_gateway,
            item_gateway)

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
            cliente_gateway: ClienteGatewayInterface,
            pagamento_gateway: PagamentoInterface) -> Pedido:
        # TODO
        # Recebe uma lista com produtos e retorna o pedido criado
        for produto in produtos_checkout.itens:
            prod = produto_gateway.retornar_pelo_id(produto.item)
            if not prod:
                raise ProdutoNotFoundException()
        cliente = cliente_gateway.retornar_pelo_id(produtos_checkout.id_cliente)
        if not cliente:
            raise ClienteNotFoundException()
        
        pedido_gateway.novo(Pedido(cliente=produtos_checkout.id_cliente))

        pedido = pedido_gateway.retornar_pelo_id(pedido_gateway.retorna_ultimo_id())

        for produto in produtos_checkout.itens:
            item_gateway.novo(Item(produto=Produto(id=produto.item), pedido=pedido, quantidade = produto.quantidade, descricao=produto.descricao))
        
        # Enviar pedido de pagamento
            
        payment_data = {
            "transaction_amount": self.retorna_valor_do_pedido(pedido.id, pedido_gateway, item_gateway, produto_gateway),
            "token": "TOKEN-ALEATORIO-TESTE",
            "description": pedido.id,
            "payment_method_id": 1,
            "notification_url":  "https://127.0.0.1/pedidos/status_pagamento/",
            "payer": {
                "email": cliente.email,
                "identification": {
                    "type": "teste", 
                    "number": "teste"
                }

            }
        }

        pagamento = pagamento_gateway.enviar_pagamento(payment_data)
        
        pedido.id_pagamento = pagamento['id_pagamento']
        pedido_gateway.editar(pedido)

        return self.ajustar_pedidos_retorno(
            [pedido_gateway.retornar_pelo_id(pedido.id)],
            pedido_gateway,
            produto_gateway,
            item_gateway)[0]
    
        
    def retorna_status_pagamento(self, pedido_id: int, pedido_gateway: PedidoGatewayInterface) -> str:
        pedido = pedido_gateway.retornar_pelo_id(pedido_id)
        if not pedido:
            raise PedidoNotFoundException()
        
        return pedido_gateway.retorna_status_pagamento(pedido_id)

    def atualiza_status_pagamento(self, status: WebhookResponseDTO, pedido_gateway: PedidoGatewayInterface):
        pedido: Pedido = pedido_gateway.retornar_pelo_id_pagamento(status.id)
        if not pedido:
            raise PedidoNotFoundException
        
        if status.action == "state_FINISHED":
            pedido.status_pagamento = 2
        elif status.action == "state_CANCELED":
            pedido.status_pagamento = 3

        pedido_gateway.editar(pedido)


    def retorna_valor_do_pedido(
            self, 
            pedido_id: int, 
            pedido_gateway: PedidoGatewayInterface,
            itens_gateway: ItemGatewayInterface,
            produtos_gateway: ProdutoGatewayInterface
            ) -> float:
        pedido = pedido_gateway.retornar_pelo_id(pedido_id)
        if not pedido or pedido == []:
            raise PedidoNotFoundException()
        # itens_no_pedido = pd.DataFrame(itens_gateway.listar_itens(pedido_id))
        # valor = itens_no_pedido["valor"].sum()
        itens_no_pedido = itens_gateway.listar_itens(pedido_id)
        valor = 0
        for item in itens_no_pedido:
            quantidade = item.quantidade
            produto = produtos_gateway.retornar_pelo_id(item.produto.id)
            valor += quantidade * produto.valor
        return valor        
            
    def ajustar_pedidos_retorno(
            self, 
            pedidos: List[Pedido],
            pedido_gateway: PedidoGatewayInterface, 
            produto_gateway: ProdutoGatewayInterface,
            item_gateway: ItemGatewayInterface):
        pedidos_retorno = []

        for p in pedidos:
            pedido: Pedido = pedido_gateway.retornar_pelo_id(p.id)
            itens: List[Item] = item_gateway.listar_itens(p.id)

            produtos = []
            for item in itens:
                produto = produto_gateway.retornar_pelo_id(item.produto.id)
                produtos.append({
                    "id" : produto.id,
                    "nome" : produto.nome,
                    "valor" : produto.valor,
                    "quantidade" : item.quantidade
                })
            
            if not pedido:
                raise PedidoNotFoundException()
            pedido_dto = PedidoDTO(
                id = pedido.id,
                status_pedido=pedido.status_pedido,
                cliente=pedido.cliente,
                datahora_recebido=pedido.datahora_recebido,
                datahora_preparacao=pedido.datahora_preparacao,
                datahora_pronto=pedido.datahora_pronto,
                datahora_finalizado=pedido.datahora_finalizado,
                status_pagamento=pedido.status_pagamento,
                id_pagamento=pedido.id_pagamento,
                itens=produtos,
                valor_total = self.retorna_valor_do_pedido(pedido.id, pedido_gateway, item_gateway, produto_gateway)
            )
            pedidos_retorno.append(pedido_dto)
        return pedidos_retorno