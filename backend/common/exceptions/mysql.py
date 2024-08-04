
class MysqlConnectionException(BaseException):
    def __init__(self, message = "Erro na conexão com o banco de dados"):
        self.message = message


class MysqlError(BaseException):
    def __init__(self, message = "Erro no banco de dados"):
        self.message = message