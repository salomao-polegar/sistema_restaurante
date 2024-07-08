from .pedido import Pedido
from .produto import Produto

class Item():
    """ Item é um produto adicionado em um pedido """
    produto: Produto
    pedido: Pedido
    quantidade: int
    valor: float
    descricao: str | None = None
    

    def __init__(self,
        produto: Produto,
        pedido: Pedido,
        quantidade: int,
        valor: float,
        descricao: str | None = None):

        self.produto = produto
        self.pedido = pedido
        self.quantidade = quantidade
        self.valor = valor
        self.descricao = descricao