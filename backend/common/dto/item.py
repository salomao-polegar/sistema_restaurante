from .pedido import PedidoDTO
from .produto import ProdutoDTO

class ItemDTO():
    pedido: int
    produto: int
    quantidade: int
    descricao: str | None

    def __init__(self, 
            pedido: int = None, 
            produto: int = None, 
            quantidade: int = 0, 
            descricao: str = None):
        self.pedido = pedido
        self.produto = produto
        self.quantidade = quantidade
        self.descricao = descricao