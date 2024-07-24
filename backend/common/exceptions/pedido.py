class PedidoNotFoundException(BaseException):
    def __init__(self, message = "Pedido não encontrado"):
        self.message = message


class PedidoAlreadyExistsException(BaseException):
    def __init__(self, message = "Pedido já existe"):
        self.message = message

class PedidoEditadoComItensException(BaseException):
    def __init__(self, message="O campo Itens não deve ser enviado ao editar um pedido"):
        self.message= message

class QuantidadeInvalidaException(BaseException):
    def __init__(self, message="A quantidade do item deve ser um inteiro positivo."):
        self.message= message