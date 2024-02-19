from pytest import fixture
from fastapi.testclient import TestClient
import services
import adapters.repositories as repositories
from domain.pedido import Pedido
from api.SingletonFastAPI import SingletonFastAPI

# # Entregável 2
# # b. APIs
# # I. Cadastro do Pedido
# # II. Identificação do Pedido via CPF

app = SingletonFastAPI.app().app
app_test = TestClient(app)

@fixture
def mysql_repo():
    repo = repositories.MysqlRepo()
    return repo

def test_pedido_database(mysql_repo):
    pedido_svc = services.PedidoService(mysql_repo)
    pedido = Pedido(
        cliente = 1
        )
    
    # TEST INSERT
    pedido_criado = pedido_svc.inserir_pedido(pedido)
    assert  (pedido_criado.id != pedido.id) and \
            (pedido_criado.cliente == pedido.cliente) and \
            (pedido_criado.status_pedido == 1)

    # TEST GET
    pedido_from_repo = pedido_svc.retornar_pedido(pedido_criado.id)
    
    
    assert (pedido_criado.id == pedido_from_repo.id) and \
           (pedido_criado.cliente == pedido_from_repo.cliente) and \
           (pedido_criado.status_pedido == pedido_from_repo.status_pedido)
    
    todos_pedidos = pedido_svc.listar_pedidos()
    assert len(todos_pedidos) > 0

    # TEST EDITA
    pedido_criado.status_pedido = 2
    
    pedido_alterado = pedido_svc.editar_pedido(pedido_criado)

    assert (pedido_criado.id == pedido_alterado.id) and \
           (pedido_criado.status_pedido == pedido_alterado.status_pedido)
           

    # TEST DELETE
    
    assert pedido_svc.deletar_pedido(pedido_alterado.id) == True
    try:
        pedido_svc.retornar_pedido(pedido_alterado.id)
        assert False
    except services.pedido.PedidoNotFoundException:
        pass


def test_endpoints_pedido():
    """ Testa o Endpoint de Pedidos"""
    
    # POST
    pedido = {
            'cliente' : 1
            }
    
    post_response = app_test.post('/pedidos/', json=pedido)
    
    assert post_response.status_code == 200
    pedido_criado = post_response.json()
    
    assert pedido_criado['cliente'] == 1
    assert pedido_criado['status_pedido'] == 1

    # GET
    assert app_test.get('/pedidos').status_code == 200
    assert app_test.get(f'/pedidos/{pedido_criado['id']}').status_code == 200

    # PUT
    pedido_criado['status_pedido']=2

    
    put_response = app_test.put(f'pedidos/', json=pedido_criado)
    
    assert put_response.status_code == 200

    pedido_alterado_response = app_test.get(f'pedidos/{pedido_criado['id']}')
    assert pedido_alterado_response.status_code == 200
    pedido_alterado = pedido_alterado_response.json()
    
    assert pedido_criado['id'] == pedido_alterado['id']
    assert pedido_criado['status_pedido'] == pedido_alterado['status_pedido']


    
    # DELETE
    delete_response = app_test.delete(f'/pedidos/{pedido_alterado['id']}')
    assert delete_response.status_code == 200
    
   
def test_checkout(mysql_repo):
    pedido_svc = services.PedidoService(mysql_repo)
    insert_pedido = Pedido(id=None, cliente=1)
    pedido_criado = pedido_svc.inserir_pedido(insert_pedido)
    fila = pedido_svc.listar_fila()
    pedido_na_fila = False

    for i in fila:
        if i['id'] == pedido_criado.id:
            pedido_na_fila = True    
    assert pedido_na_fila    
    pedido_svc.checkout(pedido_criado.id)
    pedido_na_fila = False
    fila = pedido_svc.listar_fila()
    
    for i in fila:
        print(i)
        if i['id'] == pedido_criado.id:
           assert False
    
    pedido_svc.deletar_pedido(pedido_criado.id)
    # TODO: verificar se categoria de produto existe ao criar/editar