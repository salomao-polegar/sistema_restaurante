from adapters.gateways import ProdutoGateway
from common.interfaces import DbConnection
from common.dto import ProdutoDTO
from useCases import ProdutoUseCases
from adapters.presenters import ProdutoAdapter
from typing import Dict, List

class ProdutoController:
    def listar_todos(self, dbconnection: DbConnection) -> List[Dict]:
        produtosGateway = ProdutoGateway(dbconnection)
        todosOsProdutos = ProdutoUseCases().listar_produtos(produtosGateway)
        return ProdutoAdapter.produtos_to_json(todosOsProdutos)
    
    def listar_lanches(self, dbconnection: DbConnection) -> List[Dict]:
        produto_gateway = ProdutoGateway(dbconnection)
        lanches = ProdutoUseCases().listar_lanches(produto_gateway)
        return ProdutoAdapter.produtos_to_json(lanches)
    
    def listar_acompanhamentos(self, dbconnection: DbConnection) -> List[Dict]:
        produto_gateway = ProdutoGateway(dbconnection)
        acompanhamentos = ProdutoUseCases().listar_acompanhamentos(produto_gateway)
        return ProdutoAdapter.produtos_to_json(acompanhamentos)
    
    def listar_bebidas(self, dbconnection: DbConnection) -> List[Dict]:
        produto_gateway = ProdutoGateway(dbconnection)
        bebidas = ProdutoUseCases().listar_bebidas(produto_gateway)
        return ProdutoAdapter.produtos_to_json(bebidas)
    
    def listar_sobremesas(self, dbconnection: DbConnection) -> List[Dict]:
        produto_gateway = ProdutoGateway(dbconnection)
        sobremesas = ProdutoUseCases().listar_sobremesas(produto_gateway)
        return ProdutoAdapter.produtos_to_json(sobremesas)

    def novo(self, produto_dto: ProdutoDTO,
            dbconnection: DbConnection):

        return ProdutoAdapter.produtos_to_json(ProdutoUseCases().inserir_produto(produto_dto, ProdutoGateway(dbconnection)))
    
    def retornar_pelo_id(self, db_connection: DbConnection, produto_id: int) -> List[Dict]:
        produtoGateway = ProdutoGateway(db_connection)
        retorno_produto = ProdutoUseCases().retornar_pelo_id(produto_id, produtoGateway)
        return ProdutoAdapter.produtos_to_json([retorno_produto])
    
    
    def editar(self, db_connection: DbConnection, produto_dto: ProdutoDTO) -> bool:
        
        return ProdutoUseCases().editar_produto(produto_dto, ProdutoGateway(db_connection))

    def deletar(self, db_connection: DbConnection, produto_id: int) -> bool:
        return ProdutoUseCases().deletar_produto(produto_id, ProdutoGateway(db_connection))
