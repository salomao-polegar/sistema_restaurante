from pydantic import BaseModel

class Cliente(BaseModel):
    id: int
    cpf: str | None
    nome: str | None
    email: str | None
    telefone: str | None
    ativo: bool

    