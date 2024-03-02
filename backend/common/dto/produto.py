class ProdutoDTO():
    id: int | None = None
    nome: str
    categoria: int
    valor: float
    descricao: str | None
    ativo: bool | None = None

    def __init__(self,
    id: int | None,
    nome: str,
    categoria: int,
    valor: float,
    descricao: str,
    ativo: bool | None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.valor = valor
        self.descricao = descricao
        self.ativo = ativo