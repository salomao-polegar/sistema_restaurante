from typing import List

from domain.produto import Produto
from ports.repositories.produto import ProdutoRepositoryPort
from ports.services.produto import ProdutoServicePort


class ProdutoNotFoundException(BaseException):
    def __init__(self, message = "Produto não encontrado"):
        self.message = message


class ProdutoAlreadyExistsException(BaseException):
    def __init__(self, message = "Produto já existe"):
        self.message = message

    # TODO
    # Fazer regra de negócio impedindo inserção de mesmo nome e descrição do produto

class ProdutoService(ProdutoServicePort):
    def __init__(self, repo: ProdutoRepositoryPort):
        self._repo = repo

    def inserir_produto(self, produto: Produto) -> Produto:
        _p = self._repo.retornar_produto(produto.id)
            
        if _p:
            raise ProdutoAlreadyExistsException()

        produto = self._repo.inserir_produto(produto)
        return produto
        
    def retornar_produto(self, produto_id: int) -> Produto:
        produto = self._repo.retornar_produto(produto_id)
        if not produto:
            raise ProdutoNotFoundException()
        return produto

    def listar_produtos(self) -> List[Produto]:
        return self._repo.listar_produtos()
    
    def listar_lanches(self) -> List[Produto]:
        return self._repo.listar_lanches()
    
    def listar_acompanhamentos(self) -> List[Produto]:
        return self._repo.listar_acompanhamentos()
    
    def listar_bebidas(self) -> List[Produto]:
        return self._repo.listar_bebidas()
    
    def listar_sobremesas(self) -> List[Produto]:
        return self._repo.listar_sobremesas()
    
    def editar_produto(self, produto: Produto) -> Produto:
        _p = self._repo.retornar_produto(produto.id)

        if not _p:
            raise ProdutoNotFoundException()
        
        self._repo.editar_produto(produto)
        return produto

    def deletar_produto(self, produto_id: int) -> bool:
        get_produto = self._repo.retornar_produto(produto_id)
        if not get_produto:
            raise ProdutoNotFoundException()
        self._repo.deletar_produto(produto_id)
        return True
