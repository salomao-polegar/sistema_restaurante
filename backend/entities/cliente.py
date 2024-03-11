from pydantic import BaseModel
from validate_docbr import CPF

class Cliente():
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
        # super().__init__(id = id,
        #     cpf = cpf,
        #     nome = nome,
        #     email = email,
        #     telefone = telefone,
        #     ativo = ativo)

        
        self.id: int = id
        self.cpf: str = cpf
        self.nome: str = nome
        self.email: str = email
        self.telefone: str = telefone
        self.ativo = ativo