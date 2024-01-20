from pydantic import BaseModel

class Cliente(BaseModel):
    id: int | None = None
    cpf: str | None = None
    nome: str | None = None
    email: str

    