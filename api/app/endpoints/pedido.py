from app.Entidades.Pedido import Pedido
from app.mysql_connection import get_connection
from app.SingletonFastAPI import SingletonFastAPI

app = SingletonFastAPI.app().app

### PEDIDOS ###
    
@app.get("/pedidos/")
async def get_pedidos():
    try:
        connection, cursor = get_connection()
        cursor.execute('Select * FROM pedidos')
        pedidos = cursor.fetchall()
        connection.close()
        print('DB closed')
        return { 'pedidos' : pedidos }
    except Exception as e:
        
        return {'Erro' : str(e)}

@app.get("/pedidos/{pedido_id}")
def get_pedidos(pedido_id: int):
    try:
        connection, cursor = get_connection()
        cursor.execute('Select * FROM pedidos where id=%(pedido_id)s;', ({'pedido_id':pedido_id}))
        pedido = cursor.fetchall()        
        connection.close()
        
        return {"pedido": pedido}
    except Exception as e:
        
        return {'Erro' : str(e)}

@app.post("/pedidos/")
async def salva_pedido(pedido: Pedido):
    try:
        connection, cursor = get_connection()
        cursor.execute("""INSERT INTO pedidos (status, usuario) 
                        VALUES (%(status)s, %(usuario)s);""",
                        ({'status' : pedido.status_pedido,
                          'usuario' : pedido.cliente}))
        cursor.execute("""SELECT LAST_INSERT_ID();""")
        id_pedido_inserido = cursor.fetchall()[0]['LAST_INSERT_ID()']

        connection.commit()
        connection.close()
        
        return { 'id_pedido_inserido' : id_pedido_inserido }
    except Exception as e:
        
        return {'Erro' : str(e)}

@app.delete("/pedidos/{pedido_id}")
def delete_pedido(pedido_id: int):
    try:
        connection, cursor = get_connection()
        cursor.execute('delete from pedidos where id=%(pedido_id)s;', ({'pedido_id':pedido_id}))

        connection.commit()
        connection.close()
        
        return {"resultado": "Pedido deletado com sucesso"}  
    except Exception as e:
        
        return {'Erro' : str(e)}
    
@app.post('/checkout/{pedido_id}')
def checkout_pedido(pedido_id: int):
    try:
        connection, cursor = get_connection()
        cursor.execute('update pedidos set status_pedido=1 where id=%(pedido_id)s;', 
                       ({'pedido_id':pedido_id}))
        
        connection.commit()
        connection.close()
        
        return { 'status' : 2 }    
    except Exception as e:
        
        return {'Erro' : str(e)}
