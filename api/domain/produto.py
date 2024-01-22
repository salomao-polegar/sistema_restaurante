from pydantic import BaseModel

# import json

class Produto(BaseModel):
    id: int | None = None
    nome: str
    categoria: int
    valor: float
    descricao: str | None
    ativo: bool = None