from fastapi.testclient import TestClient
from app.SingletonFastAPI import SingletonFastAPI

# Entregável 02
# b. APIs
# V. Fake checkout, apenas enviar os produtos escolhidos para a fila
# VI. Listar os pedidos

app = SingletonFastAPI.app().app
app_test = TestClient(app)

def test_get_pedidos():
    """ Testa o Endpoint de Produtos"""
    assert app_test.get('pedidos').status_code == 200

def test_envia_pedido_para_fila():
    """  """

    response = app_test.post("/pedidos/", json={
        'status_pedido' : 1,
        'cliente' : 1,
    })

    assert response.status_code == 200
    pedido_id = response.json()['id_pedido_inserido']
    assert pedido_id != 0

    # Envia pedido para preparação

    response = app_test.put(f'/pedidos/{pedido_id}', json={
        'status_pedido' : 2
    })

    # Checkout - enviar pedido para a fila
    assert app_test.get(f'/checkout/{pedido_id}').json()['status_pedido'] == 2

    assert app_test.delete(f"/pedidos/{pedido_id}") == {"resultado": "Pedido deletado com sucesso"}







    