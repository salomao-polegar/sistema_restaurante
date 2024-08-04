class ArquivoNotFoundException(BaseException):
    def __init__(self, message = "Arquivo não encontrado"):
        self.message = message