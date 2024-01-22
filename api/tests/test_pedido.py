from pytest import fixture
from fastapi.testclient import TestClient
import services
import adapters.repositories as repositories
from domain.pedido import Pedido
from app.SingletonFastAPI import SingletonFastAPI

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
    pedido_criado = pedido_svc.insert_pedido(pedido)
    assert  (pedido_criado.id != pedido.id) and \
            (pedido_criado.cliente == pedido.cliente) and \
            (pedido_criado.status_pedido == 1)

    # TEST GET
    pedido_from_repo = pedido_svc.get_pedido(pedido_criado.id)
    
    
    assert (pedido_criado.id == pedido_from_repo.id) and \
           (pedido_criado.cliente == pedido_from_repo.cliente) and \
           (pedido_criado.status_pedido == pedido_from_repo.status_pedido)
    
    todos_pedidos = pedido_svc.get_todos_pedidos()
    assert len(todos_pedidos) > 0

    # TEST EDITA
    pedido_criado.status_pedido = 2
    
    pedido_alterado = pedido_svc.edita_pedido(pedido_criado)

    assert (pedido_criado.id == pedido_alterado.id) and \
           (pedido_criado.status_pedido == pedido_alterado.status_pedido)
           

    # TEST DELETE
    
    assert pedido_svc.delete_pedido(pedido_alterado.id) == True
    try:
        pedido_svc.get_pedido(pedido_alterado.id)
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
    pedido_criado = pedido_svc.insert_pedido(insert_pedido)
    fila = pedido_svc.get_fila()
    pedido_na_fila = False

    for i in fila:
        if i['id'] == pedido_criado.id:
            pedido_na_fila = True
    
    assert pedido_na_fila
    
    pedido_svc.checkout(pedido_criado.id)
    
    pedido_na_fila = False
    fila = pedido_svc.get_fila()
    
    for i in fila:
        print(i)
        if i['id'] == pedido_criado.id:
           assert False
    
    pedido_svc.delete_pedido(pedido_criado.id)

# def test_produto_database(mysql_repo):
#     produto_svc = services.ProdutoService(mysql_repo)
#     insert_produto_id = 99999
#     insert_produto = Produto(
#         id=insert_produto_id, 
#         nome="Produto 03", 
#         categoria = 1, 
#         valor = 98.23, 
#         descricao='Descrição do produto 1', 
#         ativo=True
#         )
    
#     produto_criado = produto_svc.insert_produto(insert_produto)

#     assert  (produto_criado.id == insert_produto.id) and \
#             (produto_criado.nome == insert_produto.nome) and \
#             (produto_criado.categoria == insert_produto.categoria) and \
#             (produto_criado.valor == insert_produto.valor) and \
#             (produto_criado.descricao == insert_produto.descricao) and \
#             (produto_criado.ativo == insert_produto.ativo)

#     produto_from_repo = produto_svc.get_produto(insert_produto_id)
#     assert (insert_produto.id == produto_from_repo.id) and \
#            (insert_produto.nome == produto_from_repo.nome) and \
#            (insert_produto.categoria == produto_from_repo.categoria) and \
#            (insert_produto.valor == produto_from_repo.valor) and \
#            (insert_produto.descricao == produto_from_repo.descricao) and \
#            (insert_produto.ativo == produto_from_repo.ativo)

#     produto_svc.delete_produto(insert_produto)



# # def test_endpoints_produto():
# #     """ Testa o Endpoint de Produtos"""
# #     produto_svc = services.ProdutoService(mysql_repo)
# #     # GET
# #     assert app_test.get('/produtos').status_code == 200
# #     assert app_test.get('/lanches').status_code == 200
# #     assert app_test.get('/acompanhamentos').status_code == 200
# #     assert app_test.get('/bebidas').status_code == 200
# #     assert app_test.get('/sobremesas').status_code == 200

# #     # POST
# #     post_response = app_test.post('/produtos/',
# #         json={
# #             'nome' : 'produtotesteteste',
# #             'categoria' : 1,
# #             'valor' : 9715.27,
# #             'descricao' : 'minha descrição completa do produto',
# #             'ativo' : 1
# #         })
# #     assert post_response.status_code == 200
# #     # Fazer regra de negócio impedindo inserção de mesmo nome e descrição do produto
    
# #     produto_inserido = Produto(post_response.json())
# #     assert produto_inserido.id != 0

# #     produto_inserido_no_banco = produto_svc.get_produto(produto_inserido.id)
# #     assert produto_inserido == produto_inserido_no_banco

# #     # PUT
# #     put_response = app_test.put(f'produtos/{produto_inserido.id}',
# #             json={
# #                 'nome' : 'produtoteste_alterado',
# #                 'categoria' : 2,
# #                 'valor' : 13.13,
# #                 'descricao' : 'descricao alterada',
# #                 'ativo' : 0
# #             })
    
# #     assert put_response.status_code == 200

# #     produto_alterado = Produto(post_response.json())
# #     produto_alterado_no_banco = produto_svc.get_produto(produto_alterado.id)

# #     assert produto_alterado == produto_alterado_no_banco

# #     # DELETE
# #     delete_response = app_test.delete(f'/produtos/{produto_inserido.id}')
# #     assert delete_response == True


# def test_list_produtos(mysql_repo):
#     produto_01 = Produto(id=99999998, nome="Produto 01", categoria = 1, valor = 98.23, descricao='Descrição do produto 1', ativo=True)
#     produto_02 = Produto(id=99999999, nome="Produto 02", categoria = 2, valor = 22.23, descricao='Descrição do produto 2', ativo=True)
    
#     produto_svc = services.ProdutoService(mysql_repo)
    
#     produto_svc.insert_produto(produto_01)
#     produto_svc.insert_produto(produto_02)

#     todos_produtos = produto_svc.get_todos_produtos()
#     assert len(todos_produtos) > 0

#     produto_svc.delete_produto(produto_01)
#     produto_svc.delete_produto(produto_02)

# # # # def test_cadastro_produto():
# # # #     """ Testa o CRUD de produtos """
# # # #     response = app_test.post('/produtos/',
# # # #         json={
# # # #             'nome' : 'produtoteste',
# # # #             'categoria' : 1,
# # # #             'valor' : 9715.27,
# # # #             'descricao' : 'minha descrição completa do produto',
# # # #             'ativo' : 1
# # # #         })
# # # #     assert response.status_code == 200

# # # #     produto_id = response.json()['id_produto_inserido']
# # # #     assert produto_id != 0
    
# # # #     verificar_inclusao_no_banco = app_test.get(f'/produtos/{produto_id}')
# # # #     assert verificar_inclusao_no_banco.json()['produto'][0]['id'] == produto_id
            
# # # #     assert verificar_inclusao_no_banco.status_code == 200

# # # #     produto_alterado = app_test.put(f'produtos/{produto_id}',
# # # #             json={
# # # #                 'nome' : 'produtoteste_alterado',
# # # #                 'categoria' : 2,
# # # #                 'valor' : 13.13,
# # # #                 'descricao' : 'descricao alterada',
# # # #                 'ativo' : 0
# # # #             }).json()
# # # #     print(produto_alterado)
# # # #     assert produto_alterado['produto_alterado'] == {
# # # #                 'nome' : 'produtoteste_alterado',
# # # #                 'categoria' : 2,
# # # #                 'valor' : 13.13,
# # # #                 'descricao' : 'descricao alterada',
# # # #                 'ativo' : 0
# # # #             }

# # # #     excluir_produto_do_banco = app_test.delete(f'/produtos/{produto_id}')
# # # #     assert excluir_produto_do_banco.json() == {"resultado": "Produto deletado com sucesso"}
