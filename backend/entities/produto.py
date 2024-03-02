from pydantic import BaseModel


# import json

class Produto(BaseModel):
    id: int | None = None
    nome: str | None = None
    categoria: int | None = None
    valor: float | None = None
    descricao: str | None = None
    ativo: bool | None = None