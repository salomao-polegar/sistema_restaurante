from entities import Pedido, Item
from common.exceptions import PedidoNotFoundException, ProdutoNotFoundException, ClienteNotFoundException, PedidoEditadoComItensException, QuantidadeInvalidaException, MysqlError
from common.interfaces.gateways import PedidoGatewayInterface, ProdutoGatewayInterface, ItemGatewayInterface, ClienteGatewayInterface, PagamentoInterface   
from common.dto import PedidoCheckoutDTO, WebhookResponseDTO, PedidoDTO, PagamentoDTO
from typing import List
import uuid
import pandas as pd

class PedidoUseCases ():
    # def inserir_pedido(self, 
    #     pedido_dto: Pedido,
    #     pedido_gateway: PedidoGatewayInterface,
    #     cliente_gateway: ClienteGatewayInterface) -> bool:    

    #     if not cliente_gateway.retornar_pelo_id(pedido_dto.cliente):
    #         raise ClienteNotFoundException()

    #     pedido_gateway.novo(pedido_dto)
    #     return True      
    
    def retornar_pedido(
            self, 
            pedido_id: int, 
            pedido_gateway: PedidoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            produto_gateway: ProdutoGatewayInterface
            ) -> PedidoDTO:
        pedido = pedido_gateway.retornar_pelo_id(pedido_id)
        if not pedido:
            raise PedidoNotFoundException()
        
        return self.ajustar_pedidos_retorno(
            [pedido],
            pedido_gateway,
            produto_gateway,
            item_gateway
        )[0]

    def listar_pedidos(
            self, 
            pedido_gateway: PedidoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            produto_gateway: ProdutoGatewayInterface) -> List[PedidoDTO]:
            
            pedidos=pedido_gateway.listar_todos()
            if not pedidos: return []
            
            pedido_ajustado = self.ajustar_pedidos_retorno(
                pedidos,
                    pedido_gateway,
                    produto_gateway,
                    item_gateway
        )
            return pedido_ajustado
    
    def listar_pedidos_por_cliente_id(
            self, 
            cliente_id: str | int,
            cliente_gateway: ClienteGatewayInterface,
            pedido_gateway: PedidoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            produto_gateway: ProdutoGatewayInterface) -> List[Pedido]:
        
        

        return self.ajustar_pedidos_retorno(
            pedido_gateway.listar_pedidos_por_cliente_id(cliente_id),
            pedido_gateway,
            produto_gateway,
            item_gateway
        )

    def listar_pedidos_recebidos(self, 
            pedido_gateway: PedidoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            produto_gateway: ProdutoGatewayInterface) -> List[Pedido]:
        
        return self.ajustar_pedidos_retorno(
            pedido_gateway.listar_pedidos_por_status(1),
            pedido_gateway,
            produto_gateway,
            item_gateway)

    def listar_pedidos_em_preparacao(
            self, 
            pedido_gateway: PedidoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            produto_gateway: ProdutoGatewayInterface) -> List[Pedido]:
        
        return self.ajustar_pedidos_retorno(
            pedido_gateway.listar_pedidos_por_status(2),
            pedido_gateway,
            produto_gateway,
            item_gateway)
    
    def listar_pedidos_prontos(
            self, 
            pedido_gateway: PedidoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            produto_gateway: ProdutoGatewayInterface) -> List[Pedido]:
        
        return self.ajustar_pedidos_retorno(
            pedido_gateway.listar_pedidos_por_status(3),
            pedido_gateway,
            produto_gateway,
            item_gateway)
    
    def listar_pedidos_finalizados(self, 
            pedido_gateway: PedidoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            produto_gateway: ProdutoGatewayInterface) -> List[Pedido]:
        
        return self.ajustar_pedidos_retorno(
            pedido_gateway.listar_pedidos_por_status(4),
            pedido_gateway,
            produto_gateway,
            item_gateway)

    # def listar_pedidos_nao_finalizados(self, 
    #         pedido_gateway: PedidoGatewayInterface,
    #         item_gateway: ItemGatewayInterface,
    #         produto_gateway: ProdutoGatewayInterface) -> List[Pedido]:
        
    #     return self.ajustar_pedidos_retorno(
    #         pedido_gateway.listar_pedidos_nao_finalizados(),
    #         pedido_gateway,
    #         produto_gateway,
    #         item_gateway)

    def editar_pedido(self, 
                      pedido: Pedido, 
                      pedido_gateway: PedidoGatewayInterface,
                      item_gateway: ItemGatewayInterface,
                      produto_gateway: ProdutoGatewayInterface,
                      cliente_gateway: ClienteGatewayInterface) -> Pedido:
        
        if not pedido.id:
            raise PedidoNotFoundException()
    
        if not pedido_gateway.retornar_pelo_id(pedido.id):
            raise PedidoNotFoundException()
        
        if not pedido.cliente:
            raise ClienteNotFoundException()
        
        if not cliente_gateway.retornar_pelo_id(pedido.cliente):
            raise ClienteNotFoundException()
        
        if pedido.itens != None and pedido.itens != []:
            raise PedidoEditadoComItensException()
        
        
        
        return self.ajustar_pedidos_retorno(
            [pedido_gateway.editar(pedido)],
            pedido_gateway,
            produto_gateway,
            item_gateway)[0]
    
    # def editar_status_pedido(self, 
    #                   pedido: Pedido, 
    #                   pedido_gateway: PedidoGatewayInterface,
    #                   item_gateway: ItemGatewayInterface,
    #                   produto_gateway: ProdutoGatewayInterface
    #                   ) -> Pedido:
    #     if not pedido.id:
    #         raise PedidoNotFoundException()
    
    #     if not pedido_gateway.retornar_pelo_id(pedido.id):
    #         raise PedidoNotFoundException()
        
    #     return self.ajustar_pedidos_retorno(
    #         [pedido_gateway.editar_status_pedido(pedido)],
    #         pedido_gateway,
    #         produto_gateway,
    #         item_gateway)[0]

    def deletar_pedido(self, pedido_id: int, pedido_gateway: PedidoGatewayInterface) -> bool:
        get_pedido = pedido_gateway.retornar_pelo_id(pedido_id)
        if not get_pedido:
            raise PedidoNotFoundException()
        
        return pedido_gateway.deletar(pedido_id)

    def listar_fila(self, pedido_gateway: PedidoGatewayInterface) -> list:
        return pedido_gateway.listar_pedidos_por_status(1)

    def checkout(
            self, 
            pedido_checkout: PedidoCheckoutDTO,
            pedido_gateway: PedidoGatewayInterface, 
            produto_gateway: ProdutoGatewayInterface,
            item_gateway: ItemGatewayInterface,
            cliente_gateway: ClienteGatewayInterface,
            pagamento_gateway: PagamentoInterface) -> Pedido:
        # TODO
        # Recebe uma lista com produtos e retorna o pedido criado
        
        if not cliente_gateway.retornar_pelo_id(pedido_checkout.id_cliente): raise ClienteNotFoundException()
        
        
        pedido_gateway.novo(Pedido(
            cliente=pedido_checkout.id_cliente, 
            status_pagamento=1))
            
        pedido = pedido_gateway.retornar_pelo_id(pedido_gateway.retorna_ultimo_id())
        
        for item in pedido_checkout.itens:
            
            produto = produto_gateway.retornar_pelo_id(item.produto)
            if not produto: raise ProdutoNotFoundException()
            if not item.quantidade or not item.quantidade >=0: raise QuantidadeInvalidaException()
            novo_item = Item(produto=produto, pedido=pedido, quantidade = item.quantidade, descricao=item.descricao, valor=produto.valor)
            item_gateway.novo(novo_item)
            # pedido.itens.append(ItemPedido(
            #     valor=novo_item.valor, 
            #     descricao=novo_item.descricao, 
            #     produto=novo_item.produto.id, 
            #     quantidade=novo_item.quantidade))
        
        # Pagamento
        retorno_pagamento = pagamento_gateway.enviar_pagamento(PagamentoDTO())
        pedido.id_pagamento = retorno_pagamento['id_pagamento']
        pedido_gateway.editar(pedido)
        
        return self.ajustar_pedidos_retorno(
            [pedido], 
            pedido_gateway=pedido_gateway,
            item_gateway=item_gateway,
            produto_gateway=produto_gateway
            )[0]
    
        
    def retorna_status_pagamento(self, pedido_id: int, pedido_gateway: PedidoGatewayInterface) -> str:
        pedido = pedido_gateway.retornar_pelo_id(pedido_id)
        if not pedido: raise PedidoNotFoundException()
        
        return pedido_gateway.retorna_status_pagamento(pedido_id)

    def atualiza_status_pagamento(self, 
                                  status: WebhookResponseDTO, 
                                  pedido_gateway: PedidoGatewayInterface,
                                  item_gateway: ItemGatewayInterface,
                                  produto_gateway: ProdutoGatewayInterface,
                                  cliente_gateway: ClienteGatewayInterface
                                  ) -> Pedido:
        
        pedido = pedido_gateway.retornar_pelo_id_pagamento(status.id)
        
        if not pedido: raise PedidoNotFoundException()
        
        if status.action == "state_FINISHED":
            pedido.status_pagamento = 2
        elif status.action == "state_CANCELED":
            pedido.status_pagamento = 3

        return self.editar_pedido(pedido, pedido_gateway, item_gateway, produto_gateway, cliente_gateway)


    
            
    def ajustar_pedidos_retorno(
            self, 
            pedidos: List[Pedido],
            pedido_gateway: PedidoGatewayInterface, 
            produto_gateway: ProdutoGatewayInterface,
            item_gateway: ItemGatewayInterface) -> List[PedidoDTO]:
        pedidos_retorno = []

        for p in pedidos:
            
            itens: List[Item] = item_gateway.listar_itens(p.id)
            
            produtos = []
            valor_total = 0
            for item in itens:
                produtos.append({
                    "produto" : item.produto.id,
                    "valor" : item.valor,
                    "quantidade" : item.quantidade,
                    "descricao": item.descricao
                })
                try: 
                    valor_total += item.valor * item.quantidade
                except TypeError:
                    pass
            p.itens = produtos
            p.valor_total = valor_total
            
            pedidos_retorno.append(p)

        return pedidos_retorno
    



    # Enviar pedido de pagamento
            
        # def retorna_valor_do_pedido(
        #     self, 
        #     pedido_id: int, 
        #     pedido_gateway: PedidoGatewayInterface,
        #     itens_gateway: ItemGatewayInterface,
        #     produtos_gateway: ProdutoGatewayInterface
        #     ) -> float:
        # pedido = pedido_gateway.retornar_pelo_id(pedido_id)
        # if not pedido or pedido == []:
        #     raise PedidoNotFoundException()
        # # itens_no_pedido = pd.DataFrame(itens_gateway.listar_itens(pedido_id))
        # # valor = itens_no_pedido["valor"].sum()
        # itens_no_pedido = itens_gateway.listar_itens(pedido_id)
        # valor = 0
        # for item in itens_no_pedido:
        #     quantidade = item.quantidade
        #     produto = produtos_gateway.retornar_pelo_id(item.produto.id)
        #     valor += quantidade * produto.valor
        # return valor        
    
        # payment_data = {
        #     "transaction_amount": self.retorna_valor_do_pedido(pedido.id, pedido_gateway, item_gateway, produto_gateway),
        #     "token": "TOKEN-ALEATORIO-TESTE",
        #     "description": pedido.id,
        #     "payment_method_id": 1,
        #     "notification_url":  "https://127.0.0.1/pedidos/status_pagamento/",
        #     "payer": {
        #         "email": "cliente.email",
        #         "identification": {
        #             "type": "teste", 
        #             "number": "teste"
        #         }

        #     }
        # }

        # pagamento = pagamento_gateway.enviar_pagamento(payment_data)
        
        # pedido.id_pagamento = pagamento['id_pagamento']
        # pedido_gateway.editar(pedido)

        ######