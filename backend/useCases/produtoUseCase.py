from entities import Produto
from common.exceptions import ProdutoNotFoundException, CategoriaNotFoundException, ValorDoProdutoInvalidoException
from typing import List
from common.dto import ProdutoDTO
from common.interfaces.gateways import ProdutoGatewayInterface


class ProdutoUseCases ():
    def inserir_produto(self,
        produto_dto: ProdutoDTO,
        produto_gateway: ProdutoGatewayInterface) -> Produto:
        if produto_dto.categoria not in [1, 2, 3, 4]:
            raise CategoriaNotFoundException()
        if not produto_dto.valor > 0 or not produto_dto.valor:
            raise ValorDoProdutoInvalidoException()
        
        novo_produto = Produto(
            id = None, 
            nome= produto_dto.nome,
            categoria=produto_dto.categoria,
            valor=produto_dto.valor,
            descricao=produto_dto.descricao,
            ativo=produto_dto.ativo) 

        return produto_gateway.novo(novo_produto)
    
    def listar_produtos(self, produto_gateway: ProdutoGatewayInterface) -> List[Produto]:
        return produto_gateway.listar_todos()
    
    def listar_lanches(self, produto_gateway: ProdutoGatewayInterface) -> List[Produto]:
        return produto_gateway.listar_lanches()
    
    def listar_acompanhamentos(self, produto_gateway: ProdutoGatewayInterface) -> List[Produto]:
        return produto_gateway.listar_acompanhamentos()
    
    def listar_bebidas(self, produto_gateway: ProdutoGatewayInterface) -> List[Produto]:
        return produto_gateway.listar_bebidas()
    
    def listar_sobremesas(self, produto_gateway: ProdutoGatewayInterface) -> List[Produto]:
        return produto_gateway.listar_sobremesas()
        
    def retornar_pelo_id(self, produto_id: int, produto_gateway: ProdutoGatewayInterface) -> Produto:
        produto: Produto = produto_gateway.retornar_pelo_id(produto_id)
        if not produto: raise ProdutoNotFoundException
        return produto
    
    def editar_produto(self,
            produto_dto: ProdutoDTO,
            produto_gateway: ProdutoGatewayInterface) -> Produto:
        
        if not produto_dto.id: raise ProdutoNotFoundException
        if produto_dto.categoria not in [0, 1, 2, 3]: raise CategoriaNotFoundException()
        if not produto_dto.valor > 0 or not produto_dto.valor: raise ValorDoProdutoInvalidoException()
        
        produto = produto_gateway.retornar_pelo_id(produto_dto.id)
        if not produto: raise ProdutoNotFoundException
        
        produto_editar = Produto(
            id = produto_dto.id, 
            nome= produto_dto.nome,
            categoria=produto_dto.categoria,
            valor=produto_dto.valor,
            descricao=produto_dto.descricao,
            ativo=produto_dto.ativo)
         
        
        return produto_gateway.editar(produto_editar)

    def deletar_produto(self, produto_id: int, produto_gateway: ProdutoGatewayInterface) -> bool:
        produto_deletado = produto_gateway.retornar_pelo_id(produto_id)
        if not produto_deletado: raise ProdutoNotFoundException()
        return produto_gateway.deletar(produto_id)

