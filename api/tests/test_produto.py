from fastapi.testclient import TestClient
from app.SingletonFastAPI import SingletonFastAPI

# Entregável 02
# b. APIs
# III. Criar, editar e remover produto
# IV. Buscar produto por categoria

app = SingletonFastAPI.app().app
app_test = TestClient(app)

def test_get_produto():
    """ Testa o Endpoint de Produtos"""
    assert app_test.get('produtos').status_code == 200

def test_cadastro_produto():
    """ Testa o CRUD de produtos """
    response = app_test.post('/produtos/',
        json={
            'nome' : 'produtoteste',
            'categoria' : 1,
            'valor' : 9715.27,
            'descricao' : 'minha descrição completa do produto',
            'ativo' : 1
        })
    assert response.status_code == 200

    produto_id = response.json()['id_produto_inserido']
    assert produto_id != 0
    
    verificar_inclusao_no_banco = app_test.get(f'/produtos/{produto_id}')
    assert verificar_inclusao_no_banco.json()['produto'][0]['id'] == produto_id
            
    assert verificar_inclusao_no_banco.status_code == 200

    produto_alterado = app_test.put(f'produtos/{produto_id}',
            json={
                'nome' : 'produtoteste_alterado',
                'categoria' : 2,
                'valor' : 13.13,
                'descricao' : 'descricao alterada',
                'ativo' : 0
            }).json()
    print(produto_alterado)
    assert produto_alterado['produto_alterado'] == {
                'nome' : 'produtoteste_alterado',
                'categoria' : 2,
                'valor' : 13.13,
                'descricao' : 'descricao alterada',
                'ativo' : 0
            }

    excluir_produto_do_banco = app_test.delete(f'/produtos/{produto_id}')
    assert excluir_produto_do_banco.json() == {"resultado": "Produto deletado com sucesso"}
