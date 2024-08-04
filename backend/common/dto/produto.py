from typing import Dict
class ProdutoDTO():
    id: int | None = None
    nome: str
    categoria: int
    valor: float
    descricao: str | None
    ativo: bool | None = None
    foto_principal: str | None = None

    def __init__(self,
    id: int | None,
    nome: str,
    categoria: int,
    valor: float,
    descricao: str,
    ativo: bool | None,
    foto_principal: str | None):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.valor = valor
        self.descricao = descricao
        self.ativo = ativo
        self.foto_principal = foto_principal

    def __str__(self):
        return str([self.id, self.nome, self.categoria, self.valor, self.descricao, self.ativo, self.foto_principal])