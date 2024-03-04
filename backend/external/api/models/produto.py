from pydantic import BaseModel

class ProdutoModel(BaseModel):
    id: int | None = None
    nome: str
    categoria: int
    valor: float
    descricao: str | None
    ativo: bool | None = None