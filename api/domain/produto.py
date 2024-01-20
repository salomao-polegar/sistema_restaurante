from pydantic import BaseModel
from decimal import Decimal
# import json

class Produto(BaseModel):
    id: int | None
    nome: str
    categoria: int
    valor: Decimal
    descricao: str
    ativo: bool | None

    # def __init__(self, json_data):
    #     self.__dict__ = json.loads(json_data)