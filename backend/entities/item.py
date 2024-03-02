from pydantic import BaseModel
from .pedido import Pedido
from .produto import Produto

class Item(BaseModel):
    """ Item é um produto adicionado em um pedido """
    produto: Produto
    pedido: Pedido
    quantidade: int
    descricao: str | None = None