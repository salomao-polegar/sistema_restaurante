from typing import Protocol, List
from domain.item import Item
from ports.external.database import AppDatabasePort


class ItemRepositoryPort(Protocol):
    def __init__(self, db: AppDatabasePort):
        pass

    def listar_itens(self, pedido: int) -> List[Item]:
        pass

    def inserir_item(self, produto: Item) -> Item:
        pass

    def editar_item(self, item: Item) -> Item:
        pass

    def deletar_item(self, item: Item) -> bool:
        pass