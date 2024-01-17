from app.Entidades.Cliente import Cliente
from app.mysql_connection import get_connection
from app.SingletonFastAPI import SingletonFastAPI
app = SingletonFastAPI.app().app

### CLIENTES ###

@app.get('/clientes/', tags=['Clientes'])
def get_clientes():
    try:
        connection, cursor = get_connection()
        cursor.execute('Select * FROM clientes')
        clientes = cursor.fetchall()
        connection.close()
        # print('DB closed')
        return { 'clientes' : clientes }
    except Exception as e:
        
        return {'Erro' : str(e)}

@app.get("/clientes/{cliente_cpf}", tags=['Clientes'])
def get_cliente(cliente_cpf: str):
    
    try:
        connection, cursor = get_connection()
        cursor.execute('Select * FROM clientes where cpf=%(cliente_cpf)s', ({'cliente_cpf':cliente_cpf}))
        cliente = cursor.fetchall()        
        connection.close()
        # print('DB closed')
        return {"cliente": cliente}
    except Exception as e:
        
        return {'Erro' : str(e)}

@app.post("/clientes/", tags=['Clientes'])
async def salva_cliente(cliente: Cliente):
    try:
        connection, cursor = get_connection()
        cursor.execute("""INSERT INTO clientes (cpf, nome, email) 
                        VALUES (%(cpf)s, %(nome)s, %(email)s);""", 
                        ({'cpf': cliente.cpf,
                          'nome': cliente.nome,
                          'email': cliente.email
                          }))
        cursor.execute("""SELECT LAST_INSERT_ID();""")
        id_cliente_inserido = cursor.fetchall()[0]['LAST_INSERT_ID()']
        connection.commit()
        connection.close()
        # print('DB closed')
        return { 'cliente_inserido' : {'id':id_cliente_inserido,
                                       'cpf': cliente.cpf,
                                       'nome': cliente.nome,
                                       'email': cliente.email
                          } }
    except Exception as e:
        
        return {'Erro' : str(e)}

@app.put('/clientes/{cliente_cpf}', tags=['Clientes'])
async def edita_cliente(cliente_cpf: str, cliente: Cliente):
    try:
        connection, cursor = get_connection()
        if cliente.nome:
            cursor.execute("""UPDATE  clientes SET nome = %(nome)s
                           WHERE cpf = %(cliente_cpf)s;""", 
                        ({'nome': cliente.nome,
                          'cliente_cpf' : cliente_cpf}))
        if cliente.email:
            cursor.execute("""UPDATE  clientes SET email = %(email)s
                           WHERE id = %(cliente_cpf)s;""", 
                        ({'email': cliente.email,
                          'cliente_cpf' : cliente_cpf}))
        connection.commit()
        connection.close()
        # print('DB closed')
        return { 'cliente_alterado' : {'cpf': cliente.cpf,
                          'nome': cliente.nome,
                          'email': cliente.email
                          } }
    except Exception as e:
        
        return {'Erro' : str(e)}

@app.delete("/clientes/{cliente_cpf}", tags=['Clientes'])
def delete_cliente(cliente_cpf: str):
    try:
        connection, cursor = get_connection()
        cursor.execute('delete from clientes where cpf=%(cliente_cpf)s', ({'cliente_cpf':cliente_cpf}))
        connection.commit()
        connection.close()
        # print('DB closed')
        return {"resultado": "Cliente deletado com sucesso"}
    except Exception as e:
        
        return {'Erro' : str(e)}

