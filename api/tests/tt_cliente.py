from fastapi.testclient import TestClient
from app.SingletonFastAPI import SingletonFastAPI

# Entregável 2
# b. APIs
# I. Cadastro do Cliente
# II. Identificação do Cliente via CPF

app = SingletonFastAPI.app().app

app_test = TestClient(app)

def test_get_cliente():
    """ Testa se o endpoint 'clientes' está funcionando"""
    assert app_test.get('clientes').status_code == 200

def test_cadastro_cliente():
    """ Testa o CRUD do cliente """
    app_test.delete('/clientes/00000000000')

    response = app_test.post('/clientes/',
        json={
            'cpf' : '00000000000',
            'nome' : 'Teste Nome Cliente',
            'email' : 'testeemail7654@teste'
              })
    
    assert response.status_code == 200

    # print(response.json())

    cliente_inserido = response.json()['cliente_inserido']
    
    verificar_inclusao_no_banco = app_test.get(f'/clientes/00000000000')

    assert verificar_inclusao_no_banco.status_code == 200
    # print(verificar_inclusao_no_banco.json()['cliente'][0])
    # print(cliente_inserido)
    assert verificar_inclusao_no_banco.json()['cliente'][0] == cliente_inserido
    
    
    cliente_alterado = app_test.put(f'/clientes/00000000000', 
                                           json={
            'cpf' : '00000000000',
            'nome' : 'Teste Nome Cliente alterado',
            'email' : 'testeemail7654@teste@alterado'
              }).json()
    
    assert cliente_alterado['cliente_alterado'] == {
            'cpf' : '00000000000',
            'nome' : 'Teste Nome Cliente alterado',
            'email' : 'testeemail7654@teste@alterado'
              }


    excluir_cliente_do_banco = app_test.delete(f'/clientes/00000000000')
    assert excluir_cliente_do_banco.json() == {"resultado": "Cliente deletado com sucesso"}
