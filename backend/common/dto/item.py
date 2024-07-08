class ItemDTO():
    pedido: int
    produto: int
    quantidade: int
    valor: float
    descricao: str | None
    

    def __init__(self, 
            pedido: int = None, 
            produto: int = None, 
            quantidade: int = 0, 
            valor: float = 0,
            descricao: str = None):
        self.pedido = pedido
        self.produto = produto
        self.quantidade = quantidade
        self.valor = valor
        self.descricao = descricao
    
    def __str__(self):
        return str([self.pedido,
        self.produto,
        self.quantidade,
        self.valor,
        self.descricao])