from entities import Item
from entities.pedido import Pedido
from entities.produto import Produto
from common.exceptions import ItemNotFoundException, PedidoNotFoundException, ProdutoNotFoundException
from typing import List
from common.dto import ItemDTO, PedidoDTO, ProdutoDTO
from common.interfaces.gateways import ItemGatewayInterface, PedidoGatewayInterface, ProdutoGatewayInterface


class ItemUseCases ():
    

    def inserir_item(self,
        item_dto: ItemDTO,
        item_gateway: ItemGatewayInterface,
        produto_gateway: ProdutoGatewayInterface,
        pedido_gateway: PedidoGatewayInterface) -> bool:
        
        if not produto_gateway.retornar_pelo_id(item_dto.produto): raise ProdutoNotFoundException
        if not pedido_gateway.retornar_pelo_id(item_dto.pedido): raise PedidoNotFoundException
        busca = item_gateway.retornar_item(item_dto)[0]
        if busca:
            if item_dto.quantidade:
                busca.quantidade += item_dto.quantidade
            if item_dto.descricao:
                busca.descricao = item_dto.descricao
            item_gateway.editar(busca)
            return True

        novo_item = Item(
            pedido = Pedido(id=item_dto.pedido), 
            produto = Produto(id=item_dto.produto),
            quantidade = item_dto.quantidade,
            descricao = item_dto.descricao) 

        item_gateway.novo(novo_item)
        return True
    
    def listar_items(self, pedido_id: int, item_gateway: ItemGatewayInterface) -> List[Item]:
        return item_gateway.listar_itens(pedido_id)
    
    def retornar_item(self, item_dto: ItemDTO, item_gateway: ItemGatewayInterface):
        return item_gateway.retornar_item(item_dto)
    
    def editar_item(self,
            item_dto: ItemDTO,
            item_gateway: ItemGatewayInterface) -> True:
        if not item_gateway.listar_itens(item_dto.pedido): ItemNotFoundException
        item_editar = Item(
            pedido = Pedido(id=item_dto.pedido), 
            produto = Produto(id=item_dto.produto),
            quantidade = item_dto.quantidade,
            descricao = item_dto.descricao)
         
        item_gateway.editar(item_editar)
        return True             

    def deletar_item(self, item_dto: ItemDTO, item_gateway: ItemGatewayInterface) -> bool:
        if not item_gateway.listar_itens(item_dto.pedido): ItemNotFoundException()
        return item_gateway.deletar(item_dto)

