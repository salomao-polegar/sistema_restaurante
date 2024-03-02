class ItemNotFoundException(BaseException):
    def __init__(self, message = "Item não encontrado"):
        self.message = message