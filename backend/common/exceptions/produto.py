class ProdutoNotFoundException(BaseException):
    def __init__(self, message = "Produto não encontrado"):
        self.message = message


class ProdutoAlreadyExistsException(BaseException):
    def __init__(self, message = "Produto já existe"):
        self.message = message

class CategoriaNotFoundException(BaseException):
    def __init__(self, message = "Categoria inválida. Opções de categoria: 1 - Lanches | 2 - Bebidas | 3 - Acompanhamentos | 4 - Sobremesa."):
        self.message = message

class ValorDoProdutoInvalidoException(BaseException):
    def __init__(self, message = "Valor do produto inválido. Somente são aceitos valores decimais e positivos."):
        self.message = message