from typing import Protocol, List
from entities.item import Item
from common.dto import ItemDTO

class ItemGatewayInterface(Protocol):
    def novo(self, item_dto: ItemDTO) -> bool:
        pass
   
    def listar_itens(self, pedido_id: int) -> List[Item]:
        pass
    
    def editar(self, item_dto: ItemDTO) -> bool:
        pass

    def retornar_item(self, item_dto: ItemDTO) -> List[Item]:
        pass


    def deletar(self, item_dto: ItemDTO) -> bool:
        pass
