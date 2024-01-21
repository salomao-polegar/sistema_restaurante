from pydantic import BaseModel
from decimal import Decimal
# import json

class Produto(BaseModel):
    id: int | None
    nome: str
    categoria: int
    valor: Decimal
    descricao: str | None
    ativo: bool