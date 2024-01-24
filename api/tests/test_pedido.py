from pytest import fixture
from fastapi.testclient import TestClient
import services
import adapters.repositories as repositories
from domain.pedido import Pedido
import domain
from app.SingletonFastAPI import SingletonFastAPI
import helpers

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
    # TODO: verificar se categoria de produto existe ao criar/editar

def test_produtos_no_pedido(mysql_repo):
    # Adicionar produtos no pedido e verificar se a quantidade adiciona
    produto_svc = services.ProdutoService(mysql_repo)
    pedido_svc = services.PedidoService(mysql_repo)
    # TODO Por que 3 variáveis iguais? mysql_repo...
    produto_pedido_svc = services.ProdutoNoPedidoService(mysql_repo, mysql_repo, mysql_repo)
    
    novo_produto = domain.Produto(nome='teste', categoria=3, valor=99, descricao=None)
    novo_pedido = domain.Pedido(cliente=1)
    novo_produto = produto_svc.insert_produto(novo_produto)
    novo_pedido = pedido_svc.insert_pedido(novo_pedido)
    print('novopedido', novo_pedido)
    print('novoproduto', novo_produto)
    
    adicionar_produto1 = domain.ProdutoNoPedido(pedido = novo_pedido.id, produto = novo_produto.id, quantidade = 2)
    adicionar_produto2 = domain.ProdutoNoPedido(pedido = novo_pedido.id, produto = novo_produto.id, quantidade = 7)
    produto_pedido_svc.adicionar_produto(adicionar_produto1)
    produto_inserido = produto_pedido_svc.adicionar_produto(adicionar_produto2)
    print('produtonopedido', produto_inserido)
    todos_produtos_pedido = produto_pedido_svc.produtos_no_pedido(novo_pedido.id)
    produto = helpers.produto_no_pedido(produto_inserido.produto, todos_produtos_pedido)
    print(produto)
    assert produto != False
    assert produto.quantidade == 9

    # Editar produto
    produto.quantidade = 3
    editar = produto_pedido_svc.editar_produto(produto)
    todos_produtos_pedido = produto_pedido_svc.produtos_no_pedido(novo_pedido.id)
    assert helpers.produto_no_pedido(produto.produto, todos_produtos_pedido).quantidade == 3

    # Remover produto
    remover_produto = produto_pedido_svc.remover_produto(produto)
    assert remover_produto == True
    todos_produtos_pedido = produto_pedido_svc.produtos_no_pedido(novo_pedido.id)
    assert helpers.produto_no_pedido(editar, todos_produtos_pedido) == False
    pedido_svc.delete_pedido(novo_pedido.id)
    produto_svc.delete_produto(novo_produto.id)


def test_produtos_no_pedido_endpoint(mysql_repo):
    # Adicionar produtos no pedido e verificar se a quantidade adiciona
    novo_produto = {
            'nome' : 'produto',
            'categoria' : 1,
            'valor' : 715.27,
            'descricao' : 'minha descrição completa do produto',
            'ativo' : 1
        }
    novo_pedido = {'cliente':1}
    novo_produto = app_test.post('produtos/', json=novo_produto)
    novo_pedido = app_test.post('pedidos', json=novo_pedido)
    assert novo_pedido.status_code == 200
    assert novo_produto.status_code == 200
    novo_produto = novo_produto.json()
    novo_pedido = novo_pedido.json()

    adicionar_produto1 = {
        'pedido' : novo_pedido['id'], 
        'produto' : novo_produto['id'], 
        'quantidade' : 2}
    
    adicionar_produto2 = {
        'pedido' : novo_pedido['id'], 
        'produto' : novo_produto['id'], 
        'quantidade' : 7}

    assert app_test.post('/produtosnopedido/', json=adicionar_produto1).status_code == 200
    produto_inserido = app_test.post('/produtosnopedido/', json=adicionar_produto2)
    assert produto_inserido.status_code == 200

    produto_inserido = produto_inserido.json()
    todos_produtos_pedido = app_test.get(f'/produtosnopedido/{novo_pedido['id']}')
    assert todos_produtos_pedido.status_code == 200

    todos_produtos_pedido = todos_produtos_pedido.json()
    produto = helpers.produto_no_pedido_json(produto_inserido['produto'], todos_produtos_pedido)
    
    assert produto != False
    assert produto['quantidade'] == 9

    # Editar produto
    produto['quantidade'] = 3
    editar = app_test.put('produtosnopedido', json=
                          {
                              'produto' : produto['produto'],
                              'pedido' : produto['pedido'],
                              'quantidade' : produto['quantidade'],
                          }).json()
    todos_produtos_pedido = app_test.get(f'produtosnopedido/{novo_pedido['id']}').json()
    assert helpers.produto_no_pedido_json(produto['produto'], todos_produtos_pedido)['quantidade'] == 3

    # Remover produto
    remover_produto = app_test.delete(f"produtosnopedido/{produto['produto']}/{produto['pedido']}")

    assert remover_produto.status_code == 200
    assert bool(remover_produto) == True
    todos_produtos_pedido = app_test.get(f'produtosnopedido/{novo_pedido['id']}').json()
    assert helpers.produto_no_pedido_json(editar['produto'], todos_produtos_pedido) == False
    assert app_test.delete(f"pedidos/{novo_pedido['id']}").status_code == 200
    assert app_test.delete(f"produtos/{novo_produto['id']}").status_code == 200