class PedidoNotFoundException(BaseException):
    def __init__(self, message = "Pedido não encontrado"):
        self.message = message


class PedidoAlreadyExistsException(BaseException):
    def __init__(self, message = "Pedido já existe"):
        self.message = message