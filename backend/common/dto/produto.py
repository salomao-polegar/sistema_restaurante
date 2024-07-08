from typing import Dict
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

    def __str__(self):
        return str([self.id, self.nome, self.categoria, self.valor, self.descricao, self.ativo])