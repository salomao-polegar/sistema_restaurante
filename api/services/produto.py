from typing import List

from domain.produto import Produto
from ports.repositories.produto import ProdutoRepositoryPort
from ports.services.produto import ProdutoServicePort


class ProdutoNotFoundException(BaseException):
    pass


class ProdutoAlreadyExistsException(BaseException):
    pass

    # TODO
    # Fazer regra de negócio impedindo inserção de mesmo nome e descrição do produto

    # TODO
    # Retornar uma mensagem personalizada quando uma exceção for lançada
    # No momento, se uma exceção é lançada, o resultado é um 500 - INTERNAL SERVER ERROR
class ProdutoService(ProdutoServicePort):
    def __init__(self, repo: ProdutoRepositoryPort):
        self._repo = repo

    def get_produto(self, produto_id: int) -> Produto:
        produto = self._repo.get_produto(produto_id)
        if not produto:
            raise ProdutoNotFoundException()
        return produto

    def get_todos_produtos(self) -> List[Produto]:
        return self._repo.get_todos_produtos()
    
    def get_lanches(self) -> List[Produto]:
        return self._repo.get_lanches()
    
    def get_acompanhamentos(self) -> List[Produto]:
        return self._repo.get_acompanhamentos()
    
    def get_bebidas(self) -> List[Produto]:
        return self._repo.get_bebidas()
    
    def get_sobremesas(self) -> List[Produto]:
        return self._repo.get_sobremesas()

    def insert_produto(self, produto: Produto) -> Produto:
        _p = self._repo.get_produto(produto.id)
        
        if _p:
            raise ProdutoAlreadyExistsException()

        produto = self._repo.insert_produto(produto)
        return produto
    
    def edita_produto(self, produto: Produto) -> Produto:
        _p = self._repo.get_produto(produto.id)

        if not _p:
            raise ProdutoNotFoundException()
        
        self._repo.edita_produto(produto)
        return produto

    def delete_produto(self, produto_id: int) -> bool:
        get_produto = self._repo.get_produto(produto_id)
        if not get_produto:
            raise ProdutoNotFoundException()
        self._repo.delete_produto(produto_id)
        return True
