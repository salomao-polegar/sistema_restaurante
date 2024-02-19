import helpers
from typing import List
import domain

from ports.repositories import ItemRepositoryPort, ProdutoRepositoryPort, PedidoRepositoryPort
from ports.services.item import ItemServicePort

from services.pedido import PedidoNotFoundException
from services.produto import ProdutoNotFoundException

class ItemNotFoundException(BaseException):
    def __init__(self, message = "Item não encontrado"):
        self.message = message

class ItemService(ItemServicePort):
    """ Item é um produto adicionado em um pedido """
    def __init__(self, produto_repo: ProdutoRepositoryPort, pedido_repo: PedidoRepositoryPort, item_repo: ItemRepositoryPort):
        self._produto_repo = produto_repo
        self._pedido_repo = pedido_repo
        self._item_repo = item_repo
    
    def listar_itens(self, pedido: int) -> List[domain.Item]:
        if not self._pedido_repo.retornar_pedido(pedido):
            raise PedidoNotFoundException

        return self._item_repo.listar_itens(pedido)
        
    
    def inserir_item(self, produto: domain.Item) -> domain.Item:
        if not self._pedido_repo.retornar_pedido(produto.pedido):
            raise PedidoNotFoundException
        if not self._produto_repo.retornar_produto(produto.produto):
            raise ProdutoNotFoundException
 
        # Verifica: se já existir pedido com o mesmo produto incluído, somente aumentar a quantidade
        produtos_no_pedido = self.listar_itens(produto.pedido)
        
        verificacao =  helpers.produto_no_pedido(produto.produto, produtos_no_pedido)
        
        if verificacao != False:
            verificacao.quantidade += produto.quantidade
            return self.editar_item(verificacao)
        
        return self._item_repo.inserir_item(produto)

    def editar_item(self, item: domain.Item) -> domain.Item:
        if not self._pedido_repo.retornar_pedido(item.pedido):
            raise PedidoNotFoundException
        if not self._produto_repo.retornar_produto(item.produto):
            raise ProdutoNotFoundException
        
        return self._item_repo.editar_item(item)
    
    def deletar_item(self, item: domain.Item) -> bool:
        retorno = helpers.produto_no_pedido(item.produto, self.listar_itens(item.pedido))
        if retorno == False:
            raise ItemNotFoundException
        
        return self._item_repo.deletar_item(item)
        