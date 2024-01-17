from pydantic import BaseModel

class Produto(BaseModel):
    id: int | None = None
    nome: str
    categoria: int
    valor: float
    descricao: str
    ativo: int | None = None