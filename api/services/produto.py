from typing import List

import domain
from ports.repositories.produto import ProdutoRepositoryPort
from ports.services.produto import ProdutoServicePort


class ProdutoNotFoundException(BaseException):
    pass


class ProdutoAlreadyExistsException(BaseException):
    pass


class ProdutoService(ProdutoServicePort):
    def __init__(self, repo: ProdutoRepositoryPort):
        self._repo = repo

    def get_produto(self, produto_id) -> domain.Produto:
        produto = self._repo.get_produto(produto_id)
        if not produto:
            raise ProdutoNotFoundException()
        return produto

    def get_todos_produtos(self) -> List[domain.Produto]:
        return self._repo.get_todos_produtos()
    
    def get_lanches(self) -> List[domain.Produto]:
        return self._repo.get_lanches()
    
    def get_acompanhamentos(self) -> List[domain.Produto]:
        return self._repo.get_acompanhamentos()
    
    def get_bebidas(self) -> List[domain.Produto]:
        return self._repo.get_bebidas()
    
    def get_sobremesas(self) -> List[domain.Produto]:
        return self._repo.get_sobremesas()

    def insert_produto(self, produto: domain.Produto):
        _p = self._repo.get_produto(produto.id)
        
        if _p:
            raise ProdutoAlreadyExistsException()

        self._repo.insert_produto(produto)
        return produto
    
    def edita_produto(self, produto: domain.Produto):
        _p = self._repo.get_produto(produto.id)

        if not _p:
            raise ProdutoNotFoundException()
        
        self._repo.edita_produto(produto)
        return produto

    def delete_produto(self, produto: domain.Produto) -> bool:
        get_produto = self._repo.get_produto(produto.id)
        if not get_produto:
            raise ProdutoNotFoundException()
        self._repo.delete_produto(produto)
        return True
