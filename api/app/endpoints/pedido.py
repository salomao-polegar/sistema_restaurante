from domain.pedido import Pedido
from app.SingletonFastAPI import SingletonFastAPI
from typing import List
import adapters.repositories as repositories
import services
app = SingletonFastAPI.app().app

def mysql_repo():
    repo = repositories.MysqlRepo()
    return repo

### PEDIDOS ###

@app.post("/pedidos/", tags=['Pedidos'], response_model=Pedido)
async def salva_pedido(pedido: Pedido) -> Pedido | None:
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.insert_pedido(pedido)

@app.get("/pedidos/{pedido_id}", tags=['Pedidos'], response_model=Pedido)
def get_pedido(pedido_id: int) -> Pedido | None:
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.get_pedido(pedido_id)

@app.get("/pedidos/", tags=['Pedidos'], response_model=List[Pedido])
async def get_pedidos() -> List[Pedido] | None:
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.get_todos_pedidos()

@app.get("/pedidosrecebidos/", tags=['Pedidos'], response_model=List[Pedido])
async def get_pedidos_recebidos():
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.get_pedidos_recebidos()  

@app.get("/pedidosempreparacao/", tags=['Pedidos'], response_model=List[Pedido])
async def get_pedidos_em_preparacao():
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.get_pedidos_em_preparacao()

@app.get("/pedidosfinalizados/", tags=['Pedidos'], response_model=List[Pedido])
async def get_pedidos_finalizados():
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.get_pedidos_finalizados()
    
@app.get("/pedidosnaofinalizados/", tags=['Pedidos'], response_model=List[Pedido])
async def get_pedidos_nao_finalizados():
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.get_pedidos_nao_finalizados()

@app.put("/pedidos/", tags=['Pedidos'], response_model=Pedido)
async def edita_pedido(pedido: Pedido) -> Pedido | None:
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.edita_pedido(pedido)

@app.delete("/pedidos/", tags=['Pedidos'], response_model=Pedido)
def delete_pedido(pedido: Pedido):
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.delete_pedido(pedido)
    
# TODO
# Criar um response model com a ordem da fila
@app.get("/fila/", tags=['Pedidos']) 
async def get_fila() -> list | None:
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.get_fila()

@app.post('/checkout/{pedido_id}', tags=['Pedidos'], response_model = Pedido)
def checkout(pedido_id: int):
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.checkout(pedido_id)