from typing import List
import helpers
import domain
from ports.repositories.pedido import PedidoRepositoryPort, ProdutoNoPedidoRepositoryPort
from ports.services.pedido import PedidoServicePort, ProdutoNoPedidoServicePort
from ports.services.produto import ProdutoServicePort, ProdutoRepositoryPort
class PedidoNotFoundException(BaseException):
    pass

class PedidoAlreadyExistsException(BaseException):
    pass

class ProdutoNotFoundException(BaseException):
    pass

class ProdutoNoPedidoNotFoundException(BaseException):
    pass
class PedidoService(PedidoServicePort):
    def __init__(self, repo: PedidoRepositoryPort):
        self._repo = repo

    def insert_pedido(self, pedido: domain.Pedido) -> domain.Pedido:
        if self._repo.get_pedido(pedido.id):
            raise PedidoAlreadyExistsException()        
        return self._repo.insert_pedido(pedido)
    
    def get_pedido(self, pedido_id: int) -> domain.Pedido:
        pedido = self._repo.get_pedido(pedido_id)
        if not pedido:
            raise PedidoNotFoundException()
        return pedido

    def get_todos_pedidos(self) -> List[domain.Pedido]:
        return self._repo.get_todos_pedidos()

    def get_pedidos_recebidos(self) -> List[domain.Pedido]:
        return self._repo.get_pedidos_recebidos()

    def get_pedidos_em_preparacao(self) -> List[domain.Pedido]:
        return self._repo.get_pedidos_em_preparacao()
    
    def get_pedidos_finalizados(self) -> List[domain.Pedido]:
        return self._repo.get_pedidos_finalizados()

    def get_pedidos_nao_finalizados(self) -> List[domain.Pedido]:
        return self._repo.get_pedidos_nao_finalizados()

    def edita_pedido(self, pedido: domain.Pedido) -> domain.Pedido:
        _p = self._repo.get_pedido(pedido.id)

        if not _p:
            raise PedidoNotFoundException()
        return self._repo.edita_pedido(pedido)

    def delete_pedido(self, pedido_id: int) -> bool:
        get_pedido = self._repo.get_pedido(pedido_id)
        if not get_pedido:
            raise PedidoNotFoundException()
        
        return self._repo.delete_pedido(pedido_id)

    def get_fila(self) -> list:
        return self._repo.get_fila()

    def checkout(self, pedido_id: int) -> domain.Pedido:
        pedido = self._repo.get_pedido(pedido_id)
        if not pedido:
            raise PedidoNotFoundException()

        pedido.status_pedido = 3

        return self._repo.edita_pedido(pedido)
    
    ## Adicionando e removendo itens do pedido

class ProdutoNoPedidoService(ProdutoNoPedidoServicePort):

    def __init__(self, produto_repo: ProdutoRepositoryPort, pedido_repo: PedidoRepositoryPort, prod_ped_repo: ProdutoNoPedidoRepositoryPort):
        self._produto_repo = produto_repo
        self._pedido_repo = pedido_repo
        self._prod_ped_repo = prod_ped_repo
    
    def produtos_no_pedido(self, pedido: int) -> List[domain.ProdutoNoPedido]:
                
        return self._prod_ped_repo.produtos_no_pedido(pedido)
    
    def adicionar_produto(self, produto: domain.ProdutoNoPedido) -> domain.ProdutoNoPedido:
        if not self._pedido_repo.get_pedido(produto.pedido):
            raise PedidoNotFoundException
        if not self._produto_repo.get_produto(produto.produto):
            raise ProdutoNotFoundException
 
        # Verifica: se já existir pedido com o mesmo produto incluído, somente aumentar a quantidade
        produtos_no_pedido = self.produtos_no_pedido(produto.pedido)
        
        verificacao =  helpers.produto_no_pedido(produto.produto, produtos_no_pedido)
        
        if verificacao != False:
            verificacao.quantidade += produto.quantidade
            return self.editar_produto(verificacao)
        
        return self._prod_ped_repo.adicionar_produto(produto)

    def editar_produto(self, produto: domain.ProdutoNoPedido) -> domain.ProdutoNoPedido:
        if not self._pedido_repo.get_pedido(produto.pedido):
            raise PedidoNotFoundException
        if not self._produto_repo.get_produto(produto.produto):
            raise ProdutoNotFoundException
        
        return self._prod_ped_repo.editar_produto(produto)
    
    def remover_produto(self, produto: domain.ProdutoNoPedido) -> bool:
        print(produto)
        retorno = helpers.produto_no_pedido(produto.produto, self.produtos_no_pedido(produto.pedido))
        if retorno == False:
            raise ProdutoNoPedidoNotFoundException
        
        return self._prod_ped_repo.remover_produto(produto)
        