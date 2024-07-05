

class ClienteDTO():
    id: int
    cpf: str
    nome: str
    email: str
    hashed_password: str
    telefone: str
    ativo: bool

    def __init__(
            self,
            id: int,
            cpf: str,
            nome: str,
            email: str,
            hashed_password: str,
            telefone: str,
            ativo: bool):
        
        self.id = id
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.hashed_password = hashed_password
        self.telefone = telefone
        self.ativo = ativo

    def __str__(self):
        return str([self.id, self.cpf, self.nome, self.email, self.hashed_password, self.telefone, self.ativo])