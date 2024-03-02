# TESTS CLEAN ARCHITECTURE
from external.mysql_database import MySQLConnection
from adapters.controllers import ProdutoController
from common.dto import ProdutoDTO
from entities import ProdutoNotFoundException

def test():
    repo = MySQLConnection()

    produto_controller = ProdutoController()

    ### PRODUTOS ###
    
    produto_dto = ProdutoDTO(id=None, nome="teste produto", categoria=1, valor=921, descricao="descricao teste", ativo=1)
    
    assert produto_controller.novo(produto_dto, repo)

    # TEST GET
    produto_criado = produto_controller.retornar_pelo_id(repo, 1)[0]
    assert produto_criado is not None
    assert len(produto_controller.listar_todos(repo)) > 0
    
    # # TEST EDITA
    
    assert produto_controller.editar(repo, ProdutoDTO(
        id = 1, nome="nome alterado", categoria=2, valor=91, descricao="descricao teste alterada", ativo=0))
    
    produto_editado = produto_controller.retornar_pelo_id(repo, 1)[0]
    assert (produto_editado["id"] == 1) and \
        (produto_editado["nome"] == "nome alterado") and \
        (produto_editado["categoria"] == 2) and \
        (produto_editado["valor"] == 91) and \
        (produto_editado["descricao"] == "descricao teste alterada") and \
        (produto_editado["ativo"] == 0)
    

    # # TEST DELETE
    
    assert produto_controller.deletar(repo, 1) == True
    try:
        produto_controller.retornar_pelo_id(repo, 1)
        assert False
    except ProdutoNotFoundException:
        assert True
    