from pytest import fixture
from fastapi.testclient import TestClient
import services
import adapters.repositories as repositories
from domain.cliente import Cliente
from app.SingletonFastAPI import SingletonFastAPI

# # Entregável 2
# # b. APIs
# # I. Cadastro do Cliente
# # II. Identificação do Cliente via CPF

app = SingletonFastAPI.app().app
app_test = TestClient(app)

@fixture
def mysql_repo():
    repo = repositories.MysqlRepo()
    return repo

def test_cliente_database(mysql_repo):
    cliente_svc = services.ClienteService(mysql_repo)
    produto = Cliente(
        cpf = '09876526372',
        nome="cliente 1",
        email = 'sasa@sasa',
        telefone = '2214424232',
        ativo=True
        )
    
    # TEST INSERT
    cliente_criado = cliente_svc.insert_cliente(produto)
    assert  (cliente_criado.id != produto.id) and \
            (cliente_criado.cpf == produto.cpf) and \
            (cliente_criado.nome == produto.nome) and \
            (cliente_criado.email == produto.email) and \
            (cliente_criado.telefone == produto.telefone) and \
            (cliente_criado.ativo == produto.ativo)

    # TEST GET
    cliente_from_repo = cliente_svc.get_cliente(cliente_criado.id)
    
    
    assert (cliente_criado.id == cliente_from_repo.id) and \
           (cliente_criado.cpf == cliente_from_repo.cpf) and \
           (cliente_criado.nome == cliente_from_repo.nome) and \
           (cliente_criado.email == cliente_from_repo.email) and \
           (cliente_criado.telefone == cliente_from_repo.telefone) and \
           (cliente_criado.ativo == cliente_from_repo.ativo)
    
    todos_clientes = cliente_svc.get_todos_clientes()
    assert len(todos_clientes) > 0

    # TEST EDITA
    cliente_criado.nome = "ProdutoAlterado"
    cliente_criado.email = 'email@email.com'
    cliente_criado.telefone = '918372232'
    cliente_criado.ativo = 0

    cliente_alterado = cliente_svc.edita_cliente(cliente_criado)

    assert (cliente_criado.id == cliente_alterado.id) and \
            (cliente_criado.nome == cliente_alterado.nome) and \
           (cliente_criado.email == cliente_alterado.email) and \
           (cliente_criado.telefone == cliente_alterado.telefone) and \
           (cliente_criado.ativo == cliente_alterado.ativo)
    

    # TEST DELETE
    
    assert cliente_svc.delete_cliente(cliente_alterado.id) == True
    try:
        cliente_svc.get_cliente(cliente_alterado.id)
        assert False
    except services.cliente.ClienteNotFoundException:
        pass


# def test_endpoints_cliente():
#     """ Testa o Endpoint de Clientes"""
    
#     # POST
#     cliente = {
#             'cpf' : '00000000000',
#             'nome' : 'Teste Nome Cliente',
#             'email' : 'testeemail7654@teste',
#             'telefone' : '523534252',
#             'ativo' : True
#             }
    
#     post_response = app_test.post('/clientes/', json=cliente)
    
#     assert post_response.status_code == 200
#     cliente_criado = post_response.json()
    
#     assert cliente_criado['nome'] == cliente['nome']
#     assert cliente_criado['cpf'] == cliente['cpf']
#     assert cliente_criado['email'] == cliente['email']
#     assert cliente_criado['telefone'] == cliente['telefone']
#     assert cliente_criado['ativo'] == cliente['ativo']

#     # GET
#     assert app_test.get('/clientes').status_code == 200
#     assert app_test.get(f'/clientes/{cliente_criado['id']}')

#     # PUT
#     cliente_criado['cpf']='423423423'
#     cliente_criado['nome']='novo_nome'
#     cliente_criado['email']='fjladsfsd'
#     cliente_criado['telefone']='54332523'
#     cliente_criado['ativo']=0
    
#     put_response = app_test.put(f'clientes/',
#             json=cliente_criado)
    
#     assert put_response.status_code == 200

#     cliente_alterado_response = app_test.get(f'clientes/{cliente_criado['id']}')
#     assert cliente_alterado_response.status_code == 200
#     cliente_alterado = cliente_alterado_response.json()
    
#     assert cliente_criado['id'] == cliente_alterado['id']
#     assert cliente_criado['nome'] == cliente_alterado['nome']
#     assert cliente_criado['cpf'] == cliente_alterado['cpf']
#     assert cliente_criado['email'] == cliente_alterado['email']
#     assert cliente_criado['telefone'] == cliente_alterado['telefone']
#     assert cliente_criado['ativo'] == cliente_alterado['ativo']

    
#     # DELETE
#     delete_response = app_test.delete(f'/clientes/{cliente_alterado['id']}')
#     assert delete_response.status_code == 200
    

# from fastapi.testclient import TestClient
# from app.SingletonFastAPI import SingletonFastAPI



# app = SingletonFastAPI.app().app

# app_test = TestClient(app)

# def test_get_cliente():
#     """ Testa se o endpoint 'clientes' está funcionando"""
#     assert app_test.get('clientes').status_code == 200

# def test_cadastro_cliente():
#     """ Testa o CRUD do cliente """
#     app_test.delete('/clientes/00000000000')

#     response = app_test.post('/clientes/',
#         json={
#             'cpf' : '00000000000',
#             'nome' : 'Teste Nome Cliente',
#             'email' : 'testeemail7654@teste'
#               })
    
#     assert response.status_code == 200

#     # print(response.json())

#     cliente_inserido = response.json()['cliente_inserido']
    
#     verificar_inclusao_no_banco = app_test.get(f'/clientes/00000000000')

#     assert verificar_inclusao_no_banco.status_code == 200
#     # print(verificar_inclusao_no_banco.json()['cliente'][0])
#     # print(cliente_inserido)
#     assert verificar_inclusao_no_banco.json()['cliente'][0] == cliente_inserido
    
    
#     cliente_alterado = app_test.put(f'/clientes/00000000000', 
#                                            json={
#             'cpf' : '00000000000',
#             'nome' : 'Teste Nome Cliente alterado',
#             'email' : 'testeemail7654@teste@alterado'
#               }).json()
    
#     assert cliente_alterado['cliente_alterado'] == {
#             'cpf' : '00000000000',
#             'nome' : 'Teste Nome Cliente alterado',
#             'email' : 'testeemail7654@teste@alterado'
#               }


#     excluir_cliente_do_banco = app_test.delete(f'/clientes/00000000000')
#     assert excluir_cliente_do_banco.json() == {"resultado": "Cliente deletado com sucesso"}
