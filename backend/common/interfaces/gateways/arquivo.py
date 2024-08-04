from typing import Protocol, List
from entities.item import Item
from common.dto import ItemDTO, PedidoDTO

class ArquivoGatewayInterface(Protocol):
    def retornar_caminho_pelo_id(self, id: int) -> str:
        pass

    def adicionar_foto(self, path: str) -> int:
        pass