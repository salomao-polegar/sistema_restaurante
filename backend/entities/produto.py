from pydantic import BaseModel


# import json

class Produto():
    id: int | None = None
    nome: str | None = None
    categoria: int | None = None
    valor: float | None = None
    descricao: str | None = None
    ativo: bool | None = None
    foto_principal: bool | None = None

    def __init__(self,
            id: int | None = None,
            nome: str | None = None,
            categoria: int | None = None,
            valor: float | None = None,
            descricao: str | None = None,
            ativo: bool | None = None,
            foto_principal: bool | None = None):

        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.valor = valor
        self.descricao = descricao
        self.ativo = ativo
        self.foto_principal = foto_principal
        
    def __str__(self):
        return str([self.id, self.nome, self.categoria, self.valor, self.descricao, self.ativo, self.foto_principal])