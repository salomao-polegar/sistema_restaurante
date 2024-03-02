

class ClienteDTO():
    id: int
    cpf: str
    nome: str
    email: str
    telefone: str
    ativo: bool

    def __init__(
            self,
            id: int,
            cpf: str,
            nome: str,
            email: str,
            telefone: str,
            ativo: bool):
        
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.ativo = ativo