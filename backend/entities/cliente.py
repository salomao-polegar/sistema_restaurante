from pydantic import BaseModel
from validate_docbr import CPF

class Cliente(BaseModel):
    id: int | None = None
    cpf: str | None = None
    nome: str | None = None
    email: str | None = None
    telefone: str | None = None
    ativo: bool = True

    def __init__(self,
        id: str | None = None,
        cpf: str | None = None,
        nome: str | None = None,
        email: str | None = None,
        telefone: str | None = None,
        ativo: bool = True):
        # if not CPF().validate(cpf): raise CPFInvalidoException
        super().__init__(id = id,
            cpf = cpf,
            nome = nome,
            email = email,
            telefone = telefone,
            ativo = ativo)
        
