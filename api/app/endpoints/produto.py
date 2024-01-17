from app.Entidades.Produto import Produto
from app.mysql_connection import get_connection
from app.SingletonFastAPI import SingletonFastAPI
from typing import List

app = SingletonFastAPI.app().app

### PRODUTOS ###

@app.get("/produtos/", tags=['Produtos'], response_model=List[Produto])
async def get_produtos():
    try:
        connection, cursor = get_connection()
        cursor.execute('Select * FROM produtos')
        produtos = cursor.fetchall()
        connection.close()
        return { 'produtos' : produtos }
    except Exception as e:
        
        return {'Erro' : str(e)}

@app.get("/produtos/{produto_id}", tags=['Produtos'], response_model=List[Produto])
def get_produto(produto_id: int):
    try:
        connection, cursor = get_connection()
        cursor.execute('Select * FROM produtos where id=%(produto_id)s', ({'produto_id':produto_id}))
        produto = cursor.fetchall()        
        connection.close()
        return {"produto": produto}
    except Exception as e:
        
        return {'Erro' : str(e)}

@app.post("/produtos/", tags=['Produtos'])
async def salva_produto(produto: Produto):
    try:
        connection, cursor = get_connection()
        cursor.execute("""INSERT INTO produtos (nome, categoria, valor, descricao, ativo) 
                        VALUES (%(nome)s, %(categoria)s, %(valor)s, %(descricao)s, 1)""", 
                        ({'nome': produto.nome,
                          'categoria': produto.categoria,
                          'valor': produto.valor,
                          'descricao': produto.descricao,
                          }))
        cursor.execute("""SELECT LAST_INSERT_ID();""")
        id_produto_inserido = cursor.fetchall()[0]['LAST_INSERT_ID()']
        connection.commit()
        connection.close()
        return { 'id_produto_inserido' : id_produto_inserido }
    except Exception as e:
        
        return {'Erro' : str(e)}
    
@app.put("/produtos/{produto_id}", tags=['Produtos'])
async def edita_produto(produto_id: int, produto: Produto):
    try:
        connection, cursor = get_connection()
        if produto.nome:
            cursor.execute("""UPDATE produtos SET nome = %(nome)s 
                           WHERE id = %(id)s;""", 
                           ({'nome' : produto.nome,
                             'id' : produto_id}))

        if produto.categoria:
            cursor.execute("""UPDATE produtos SET categoria = %(categoria)s 
                           WHERE id = %(id)s;""", 
                           ({'categoria' : produto.categoria,
                             'id' : produto_id}))

        if produto.valor:
            cursor.execute("""UPDATE produtos SET valor = %(valor)s 
                           WHERE id = %(id)s;""", 
                           ({'valor' : produto.valor,
                             'id' : produto_id}))
        if produto.descricao:
            cursor.execute("""UPDATE produtos SET descricao = %(descricao)s 
                           WHERE id = %(id)s;""", 
                           ({'descricao' : produto.descricao,
                             'id' : produto_id}))
        if produto.ativo:
            cursor.execute("""UPDATE produtos SET ativo = %(ativo)s 
                           WHERE id = %(id)s;""", 
                           ({'ativo' : produto.ativo,
                             'id' : produto_id}))

        connection.commit()
        connection.close()

        return { 'produto_alterado' : {'nome': produto.nome,
                          'categoria': produto.categoria,
                          'valor': produto.valor,
                          'descricao': produto.descricao,
                          'ativo' : produto.ativo
                          } }
    except Exception as e:
        
        return {'Erro' : str(e)}

@app.delete("/produtos/{produto_id}", tags=['Produtos'])
def delete_produto(produto_id: int):
    try:
        connection, cursor = get_connection()
        cursor.execute('delete from produtos where id=%(produto_id)s', ({'produto_id':produto_id}))
        connection.commit()
        connection.close()
        return {"resultado": "Produto deletado com sucesso"}
    except Exception as e:
        
        return {'Erro' : str(e)}
    
@app.get("/lanches/", tags=['Produtos'], response_model=List[Produto])
async def get_lanche():
    try:
        connection, cursor = get_connection()
        cursor.execute("Select * FROM produtos where categoria = 1")
        lanches = cursor.fetchall()
        connection.close()
        return { 'lanches' : lanches }
    except Exception as e:
        
        return {'Erro' : str(e)}    

@app.get("/acompanhamentos/", tags=['Produtos'], response_model=List[Produto])
async def get_acompanhamentos():
    try:
        connection, cursor = get_connection()
        cursor.execute("Select * FROM produtos where categoria = 2")
        acompanhamentos = cursor.fetchall()
        connection.close()
        return { 'acompanhamentos' : acompanhamentos }
    except Exception as e:
        
        return {'Erro' : str(e)}

@app.get("/bebidas/", tags=['Produtos'], response_model=List[Produto])
async def get_bebidas():
    try:
        connection, cursor = get_connection()
        cursor.execute("Select * FROM produtos where categoria = 3")
        bebidas = cursor.fetchall()
        connection.close()
        return { 'bebidas' : bebidas }
    except Exception as e:
        
        return {'Erro' : str(e)}
    
@app.get("/sobremesas/", tags=['Produtos'], response_model=List[Produto])
async def get_sobremesas():
    try:
        connection, cursor = get_connection()
        cursor.execute("Select * FROM produtos where categoria = 4")
        sobremesas = cursor.fetchall()
        connection.close()
        return { 'sobremesas' : sobremesas }
    except Exception as e:
        
        return {'Erro' : str(e)}    
