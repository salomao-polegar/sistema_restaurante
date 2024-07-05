class ClienteNotFoundException(BaseException):
    def __init__(self, message = "Cliente não encontrado"):
        self.message = message

class ClienteAlreadyExistsException(BaseException):
    def __init__(self, message = "CPF já cadastrado"):
        self.message = message

class CPFInvalidoException(BaseException):
    def __init__(self, message = "CPF inválido"):
        self.message = message