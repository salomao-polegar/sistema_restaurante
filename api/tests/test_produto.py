from pytest import fixture
from fastapi.testclient import TestClient
import services, uuid
import adapters.repositories as repositories
from domain.produto import Produto
from app.SingletonFastAPI import SingletonFastAPI

# Entregável 02
# b. APIs
# III. Criar, editar e remover produto
# IV. Buscar produto por categoria

app = SingletonFastAPI.app().app
app_test = TestClient(app)

@fixture
def mysql_repo():
    repo = repositories.MysqlRepo()
    return repo

def test_produto_database(mysql_repo):
    produto_svc = services.ProdutoService(mysql_repo)
    produto = Produto(
        id=None, 
        nome="Produto 03", 
        categoria = 1, 
        valor = 98.23, 
        descricao='Descrição do produto 1', 
        ativo=True
        )
    
    # TEST INSERT
    produto_criado = produto_svc.insert_produto(produto)
    assert  (produto_criado.id != produto.id) and \
            (produto_criado.nome == produto.nome) and \
            (produto_criado.categoria == produto.categoria) and \
            (produto_criado.valor == produto.valor) and \
            (produto_criado.descricao == produto.descricao) and \
            (produto_criado.ativo == produto.ativo)

    # TEST GET
    produto_from_repo = produto_svc.get_produto(produto_criado.id)
    
    
    assert (produto_criado.id == produto_from_repo.id) and \
           (produto_criado.nome == produto_from_repo.nome) and \
           (produto_criado.categoria == produto_from_repo.categoria) and \
           (produto_criado.valor == produto_from_repo.valor) and \
           (produto_criado.descricao == produto_from_repo.descricao) and \
           (produto_criado.ativo == produto_from_repo.ativo)
    
    todos_produtos = produto_svc.get_todos_produtos()
    assert len(todos_produtos) > 0

    # TEST EDITA
    produto_criado.nome = "ProdutoAlterado"
    produto_criado.categoria = 2
    produto_criado.valor = 91.82
    produto_criado.descricao = "DescriçãoAlterada"
    produto_criado.ativo = 0

    produto_alterado = produto_svc.edita_produto(produto_criado)

    assert (produto_criado.id == produto_alterado.id) and \
           (produto_criado.nome == produto_alterado.nome) and \
           (produto_criado.categoria == produto_alterado.categoria) and \
           (produto_criado.valor == produto_alterado.valor) and \
           (produto_criado.descricao == produto_alterado.descricao) and \
           (produto_criado.ativo == produto_alterado.ativo)
    

    # TEST DELETE
    
    assert produto_svc.delete_produto(produto_alterado.id) == True
    try:
        produto_svc.get_produto(produto_alterado.id)
        assert False
    except services.produto.ProdutoNotFoundException:
        pass


def test_endpoints_produto():
    """ Testa o Endpoint de Produtos"""
    
    # POST
    produto = {
            'nome' : 'produto',
            'categoria' : 1,
            'valor' : 715.27,
            'descricao' : 'minha descrição completa do produto',
            'ativo' : 1
        }
    
    post_response = app_test.post('/produtos/', json=produto)
    
    assert post_response.status_code == 200
    produto_criado = post_response.json()
    
    assert produto_criado['nome'] == produto['nome']
    assert produto_criado['categoria'] == produto['categoria']
    assert produto_criado['valor'] == produto['valor']
    assert produto_criado['descricao'] == produto['descricao']
    assert produto_criado['ativo'] == produto['ativo']

    # GET
    assert app_test.get('/produtos').status_code == 200
    assert app_test.get(f'/produtos/{produto_criado['id']}')
    assert app_test.get('/lanches').status_code == 200
    assert app_test.get('/acompanhamentos').status_code == 200
    assert app_test.get('/bebidas').status_code == 200
    assert app_test.get('/sobremesas').status_code == 200

    # PUT
    produto_criado['nome']='produto_alterado'
    produto_criado['categoria']=2
    produto_criado['valor']=99.10
    produto_criado['descricao']='descrição alterada'
    produto_criado['ativo']=0
    
    put_response = app_test.put(f'produtos/',
            json=produto_criado)
    
    assert put_response.status_code == 200

    produto_alterado_response = app_test.get(f'produtos/{produto_criado['id']}')
    assert produto_alterado_response.status_code == 200
    produto_alterado = produto_alterado_response.json()
    
    assert produto_criado['id'] == produto_alterado['id']
    assert produto_criado['nome'] == produto_alterado['nome']
    assert produto_criado['categoria'] == produto_alterado['categoria']
    assert produto_criado['valor'] == produto_alterado['valor']
    assert produto_criado['descricao'] == produto_alterado['descricao']
    assert produto_criado['ativo'] == produto_alterado['ativo']

    
    # DELETE
    delete_response = app_test.delete(f'/produtos/{produto_alterado['id']}')
    assert delete_response.status_code == 200
    