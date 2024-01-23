import domain
from typing import List

def produto_no_pedido(produto: int, produtos_no_pedido: List[domain.ProdutoNoPedido]) -> domain.ProdutoNoPedido | bool:
    """ Verifica se determinado produto está em uma lista de produtos de um pedido """
    
    for i in produtos_no_pedido:

        if produto == i.produto:
            return i

    return False       