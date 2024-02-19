from pydantic import BaseModel

class Item(BaseModel):
    """ Item é um produto adicionado em um pedido """
    produto: int
    pedido: int
    quantidade: int
    observacoes: str | None = None