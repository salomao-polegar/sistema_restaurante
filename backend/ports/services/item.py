
from typing import Protocol, List
from domain.item import Item
from ports.repositories.item import ItemRepositoryPort

class ItemServicePort(Protocol):
    def __init__(self, repo: ItemRepositoryPort):
        pass

    def listar_itens(self, pedido: int) -> List[Item]:
        pass
    
    def inserir_item(self, item: Item) -> Item:
        pass

    def editar_item(self, item: Item) -> Item:
        pass        

    def deletar_item(self, item: Item) -> bool:
        pass