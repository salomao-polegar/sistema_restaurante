import domain
from typing import List

def produto_no_pedido(produto: int, produtos_no_pedido: List[domain.Item]) -> domain.Item | bool:
    """ Verifica se determinado produto está em uma lista de produtos de um pedido """
    
    for i in produtos_no_pedido:
        print(produto, "==", i)
        if produto == i.produto:
            print(produto, "==", i.produto)
            print('return', i)
            return i

    return False  

def produto_no_pedido_json(produto: int, produtos_no_pedido: List[dict]) -> domain.Item | bool:
    """ Verifica se determinado produto está em uma lista de produtos de um pedido """
    
    for i in produtos_no_pedido:
        if produto == i['produto']:
            return i

    return False       