# TESTS CLEAN ARCHITECTURE
from external.mysql_database import MySQLConnection
from adapters.controllers import ClienteController
from common.dto import ClienteDTO
from entities import ClienteNotFoundException

def test():
    repo = MySQLConnection()

    cliente_controller = ClienteController()

    ### CLIENTES ###
    cliente_cpf = '09876526372'
    cliente_dto = ClienteDTO(8876,
        cpf = cliente_cpf,
        nome="cliente 1",
        email = 'sasa@sasa',
        telefone = '2214424232',
        ativo=True
        )
    
    assert cliente_controller.novo(cliente_dto, repo)

    # TEST GET
    cliente_criado = cliente_controller.retornar_pelo_cpf(repo, cliente_cpf)[0]
    assert cliente_criado is not None
    assert len(cliente_controller.listar_todos(repo)) > 0
    
    # # TEST EDITA
    
    assert cliente_controller.editar(repo, ClienteDTO(
        id = cliente_criado['id'],
        cpf = "09312109212",
        nome = "Cliente alterado",
        email = "email@editado",
        telefone = "0987654321",
        ativo = 0
        ))
    cliente_editado = cliente_controller.retornar_pelo_id(repo, cliente_criado["id"])[0]
    assert (cliente_editado["id"] == cliente_criado["id"]) and \
        (cliente_editado["cpf"] == "09312109212") and \
        (cliente_editado["nome"] == "Cliente alterado") and \
        (cliente_editado["email"] == "email@editado") and \
        (cliente_editado["telefone"] == "0987654321") and \
        (cliente_editado["ativo"] == 0)
    

    # # TEST DELETE
    
    assert cliente_controller.deletar(repo, cliente_criado["id"]) == True
    try:
        cliente_controller.retornar_pelo_id(repo, cliente_criado["id"])
        assert False
    except ClienteNotFoundException:
        assert True
    