class ParametroBd:
    campo: str
    valor: any

    def __init__(self, campo: str, valor: any):
        self.campo = campo
        self.valor = valor