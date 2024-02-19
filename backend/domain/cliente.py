from pydantic import BaseModel

class Cliente(BaseModel):
    id: int | None = None
    cpf: str | None = None
    nome: str | None = None
    email: str | None = None
    telefone: str | None = None
    ativo: bool = True

    