from adapters.gateways import ItemGateway, ProdutoGateway, PedidoGateway
from common.interfaces import DbConnection
from common.dto import ItemDTO
from useCases import ItemUseCases
from adapters.presenters import ItemAdapter
from typing import Dict, List

class ItemController:
    def listar_itens(self, dbconnection: DbConnection, pedido_id: int) -> List[Dict]:
        itemsGateway = ItemGateway(dbconnection)
        todosOsItems = ItemUseCases().listar_items(pedido_id, itemsGateway)
        return ItemAdapter.items_to_json(todosOsItems)

    def novo(self, item_dto: ItemDTO,
            dbconnection: DbConnection):

        return ItemAdapter.items_to_json(
            ItemUseCases().inserir_item(
                item_dto, 
                ItemGateway(dbconnection), 
                ProdutoGateway(dbconnection), 
                PedidoGateway(dbconnection)))
    
    
    def editar(self, db_connection: DbConnection, item_dto: ItemDTO) -> bool:
        
        return ItemUseCases().editar_item(item_dto, ItemGateway(db_connection))

    def deletar(self, db_connection: DbConnection, item_dto: ItemDTO) -> bool:
        return ItemUseCases().deletar_item(item_dto, ItemGateway(db_connection))
