from common.interfaces.dbconnection import DbConnection
from common.interfaces.gateways import ArquivoGatewayInterface
from common.tipos import ParametroBd

class ArquivoGateway (ArquivoGatewayInterface):
    repositorio: DbConnection
    
    def __init__(self, repositorio: DbConnection):
        self.repositorio = repositorio
    
    def retornar_caminho_pelo_id(self, id: int) -> str:
        
        retornoBd = self.repositorio.buscar_por_parametros(
            "fotos",
            None,
            [ParametroBd(campo = "id", valor = id)])

        if retornoBd == None: return None
        if len(retornoBd) < 1: return None

        p = retornoBd[0]
        return p['caminho']
    
    def adicionar_foto(self, path: str) -> int:

        self.repositorio.inserir(
            "fotos", 
            [ParametroBd(campo = "caminho", valor=path)]
        )

        id_inserido = self.repositorio.retorna_ultimo_id("fotos")
        
        return id_inserido