from common.interfaces import DbConnection
from adapters.gateways import ArquivoGateway
from useCases.arquivoUseCase import ArquivoUseCases

class ArquivoController:
    def retornar_caminho_pelo_id(self, dbconnection: DbConnection, id: int) -> str:
        arquivo_gateway = ArquivoGateway(dbconnection)
        return ArquivoUseCases().retornar_caminho_pelo_id(id, arquivo_gateway)
        
    def adicionar_foto(self, dbconnection: DbConnection, path: str) -> int:
        arquivo_gateway = ArquivoGateway(dbconnection)
        return ArquivoUseCases().adicionar_foto(path, arquivo_gateway)
    