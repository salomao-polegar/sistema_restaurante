from entities import Produto
from common.exceptions import ProdutoNotFoundException, CategoriaNotFoundException, ValorDoProdutoInvalidoException, ArquivoNotFoundException
from typing import List
from common.dto import ProdutoDTO
from common.interfaces.gateways import ArquivoGatewayInterface


class ArquivoUseCases ():
    def retornar_caminho_pelo_id(self, id: int, arquivo_gateway: ArquivoGatewayInterface) -> str:
        
        path: str = arquivo_gateway.retornar_caminho_pelo_id(id)
        if not path: raise ArquivoNotFoundException
        return path
    
    def adicionar_foto(self, path:str, arquivo_gateway: ArquivoGatewayInterface) -> int:

        return arquivo_gateway.adicionar_foto(path)