from pytest import fixture
from fastapi.testclient import TestClient
import services
import adapters.repositories as repositories
import domain
from api.SingletonFastAPI import SingletonFastAPI
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

def test_item(mysql_repo):
    # Adicionar itens no pedido e verificar se a quantidade adiciona
    produto_svc = services.ProdutoService(mysql_repo)
    pedido_svc = services.PedidoService(mysql_repo)
    # TODO Por que 3 variáveis iguais? mysql_repo...
    item_svc = services.ItemService(mysql_repo, mysql_repo, mysql_repo)
    
    novo_produto = domain.Produto(nome='teste', categoria=3, valor=99, descricao=None)
    novo_pedido = domain.Pedido(cliente=1)
    novo_produto = produto_svc.inserir_produto(novo_produto)
    novo_pedido = pedido_svc.inserir_pedido(novo_pedido)
    
    adicionar_item_1 = domain.Item(pedido = novo_pedido.id, produto = novo_produto.id, quantidade = 2)
    adicionar_item_2 = domain.Item(pedido = novo_pedido.id, produto = novo_produto.id, quantidade = 7)
    item_svc.inserir_item(adicionar_item_1)

    item_inserido = item_svc.inserir_item(adicionar_item_2)
    
    todos_itens = item_svc.listar_itens(novo_pedido.id)
    item = helpers.produto_no_pedido(item_inserido.produto, todos_itens)
    assert item != False
    assert item.quantidade == 9

    # Editar item
    item.quantidade = 3
    editar = item_svc.editar_item(item)
    todos_itens = item_svc.listar_itens(novo_pedido.id)
    assert helpers.produto_no_pedido(item.produto, todos_itens).quantidade == 3

    # Remover item
    remover_produto = item_svc.deletar_item(item)
    assert remover_produto == True
    todos_itens = item_svc.listar_itens(novo_pedido.id)
    assert helpers.produto_no_pedido(editar, todos_itens) == False
    pedido_svc.deletar_pedido(novo_pedido.id)
    produto_svc.deletar_produto(novo_produto.id)


def test_item_endpoint(mysql_repo):
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

    adicionar_item_1 = {
        'pedido' : novo_pedido['id'], 
        'produto' : novo_produto['id'], 
        'quantidade' : 2}
    
    adicionar_item_2 = {
        'pedido' : novo_pedido['id'], 
        'produto' : novo_produto['id'], 
        'quantidade' : 7}

    assert app_test.post('/item/', json=adicionar_item_1).status_code == 200
    item_inserido = app_test.post('/item/', json=adicionar_item_2)
    assert item_inserido.status_code == 200

    item_inserido = item_inserido.json()
    todos_itens = app_test.get(f'/item/{novo_pedido['id']}')
    assert todos_itens.status_code == 200

    todos_itens = todos_itens.json()
    item = helpers.produto_no_pedido_json(item_inserido['produto'], todos_itens)
    
    assert item != False
    assert item['quantidade'] == 9

    # Editar produto
    item['quantidade'] = 3
    editar = app_test.put('/item/', json=
                          {
                              'produto' : item['produto'],
                              'pedido' : item['pedido'],
                              'quantidade' : item['quantidade'],
                          }).json()
    todos_itens = app_test.get(f'item/{novo_pedido['id']}').json()
    assert helpers.produto_no_pedido_json(item['produto'], todos_itens)['quantidade'] == 3

    # Remover produto
    remover_item = app_test.delete(f"item/{item['pedido']}/{item['produto']}")

    assert remover_item.status_code == 200
    assert bool(remover_item) == True
    todos_itens = app_test.get(f'item/{novo_pedido['id']}').json()
    assert helpers.produto_no_pedido_json(editar['produto'], todos_itens) == False
    assert app_test.delete(f"pedidos/{novo_pedido['id']}").status_code == 200
    assert app_test.delete(f"produtos/{novo_produto['id']}").status_code == 200