class ProdutoNotFoundException(BaseException):
    def __init__(self, message = "Produto não encontrado"):
        self.message = message


class ProdutoAlreadyExistsException(BaseException):
    def __init__(self, message = "Produto já existe"):
        self.message = message