from pydantic import BaseModel


# import json

class Produto():
    id: int | None = None
    nome: str | None = None
    categoria: int | None = None
    valor: float | None = None
    descricao: str | None = None
    ativo: bool | None = None

    def __init__(self,
            id: int | None = None,
            nome: str | None = None,
            categoria: int | None = None,
            valor: float | None = None,
            descricao: str | None = None,
            ativo: bool | None = None):

        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.valor = valor
        self.descricao = descricao
        self.ativo = ativo
        