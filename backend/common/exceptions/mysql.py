
class MysqlConnectionException(BaseException):
    def __init__(self, message = "Erro no banco de dados"):
        self.message = message