from app.Entidades.Pedido import Pedido
from app.mysql_connection import get_connection
from app.SingletonFastAPI import SingletonFastAPI
import pandas as pd
from typing import List
from json import loads

app = SingletonFastAPI.app().app

### PEDIDOS ###
    
@app.get("/pedidos/", tags=['Pedidos'], response_model=List[Pedido])
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

@app.get("/pedidos/{pedido_id}", tags=['Pedidos'], response_model=List[Pedido])
def get_pedidos(pedido_id: int):
    try:
        connection, cursor = get_connection()
        cursor.execute('Select * FROM pedidos where id=%(pedido_id)s;', ({'pedido_id':pedido_id}))
        pedido = cursor.fetchall()        
        connection.close()
        
        return {"pedido": pedido}
    except Exception as e:
        
        return {'Erro' : str(e)}

@app.post("/pedidos/", tags=['Pedidos'])
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

@app.delete("/pedidos/{pedido_id}", tags=['Pedidos'])
def delete_pedido(pedido_id: int):
    try:
        connection, cursor = get_connection()
        cursor.execute('delete from pedidos where id=%(pedido_id)s;', ({'pedido_id':pedido_id}))

        connection.commit()
        connection.close()
        
        return {"resultado": "Pedido deletado com sucesso"}  
    except Exception as e:
        
        return {'Erro' : str(e)}
    
@app.post('/checkout/{pedido_id}', tags=['Pedidos'])
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

@app.get('/fila/', tags=['Pedidos'], response_model=List[Pedido])
def mostra_fila():
    try:
        connection, cursor = get_connection()
        cursor.execute('select * from pedidos where status_pedido=1 ORDER BY id;')
        fila_pedidos = cursor.fetchall()
        connection.commit()
        connection.close()
        fila_df = pd.DataFrame(fila_pedidos)[['id', 'cliente', 'datahora_pedido']]
        fila_df['posicao'] = fila_df.index
        fila_df['posicao'] = fila_df['posicao'].apply(lambda x: x+1)
        #print(fila_df)
        return (loads(fila_df.to_json(orient='records')))
    except Exception as e:
        
        return {'Erro' : str(e)}
