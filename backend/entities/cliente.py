# from common.exceptions.cliente import CPFInvalidoException
# from validate_docbr import CPF

# class Endereco():
#     cep: str
#     rua: str
#     numero: str
#     complemento: str
#     estado: str

class Cliente():
    id: int | None = None
    cpf: str | None = None
    nome: str | None = None
    email: str | None = None
    hashed_password: str | None = None
    telefone: str | None = None
    ativo: bool = True
    # endereco: Endereco | None = None

    def __init__(self,
        id: str | None = None,
        cpf: str | None = None,
        nome: str | None = None,
        email: str | None = None,
        telefone: str | None = None,
        ativo: bool = True,
        hashed_password: str | None = None,
        # endereco: Endereco | None = None
        ):
        # if not CPF().validate(cpf): raise CPFInvalidoException
        
        self.id: int = id
        self.cpf: str = cpf
        self.nome: str = nome
        self.email: str = email
        self.hashed_password: str = hashed_password
        self.telefone: str = telefone
        self.ativo = ativo