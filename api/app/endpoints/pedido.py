import domain
from app.SingletonFastAPI import SingletonFastAPI
from typing import List
import adapters.repositories as repositories
import services
app = SingletonFastAPI.app().app

def mysql_repo():
    repo = repositories.MysqlRepo()
    return repo

### PEDIDOS ###

@app.post("/pedidos/", tags=['Pedidos'], response_model=domain.Pedido)
async def salva_pedido(pedido: domain.Pedido) -> domain.Pedido | None:
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.insert_pedido(pedido)

@app.get("/pedidos/{pedido_id}", tags=['Pedidos'], response_model=domain.Pedido)
def get_pedido(pedido_id: int) -> domain.Pedido | None:
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.get_pedido(pedido_id)

@app.get("/pedidos/", tags=['Pedidos'], response_model=List[domain.Pedido])
async def get_pedidos() -> List[domain.Pedido] | None:
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.get_todos_pedidos()

@app.get("/pedidos/recebidos/", tags=['Pedidos'], response_model=List[domain.Pedido])
async def get_pedidos_recebidos():
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.get_pedidos_recebidos()  

@app.get("/pedidos/empreparacao/", tags=['Pedidos'], response_model=List[domain.Pedido])
async def get_pedidos_em_preparacao():
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.get_pedidos_em_preparacao()

@app.get("/pedidos/finalizados/", tags=['Pedidos'], response_model=List[domain.Pedido])
async def get_pedidos_finalizados():
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.get_pedidos_finalizados()
    
@app.get("/pedidos/naofinalizados/", tags=['Pedidos'], response_model=List[domain.Pedido])
async def get_pedidos_nao_finalizados():
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.get_pedidos_nao_finalizados()

@app.put("/pedidos/", tags=['Pedidos'], response_model=domain.Pedido)
async def edita_pedido(pedido: domain.Pedido) -> domain.Pedido | None:
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.edita_pedido(pedido)

@app.delete("/pedidos/{pedido_id}", tags=['Pedidos'])
def delete_pedido(pedido_id: int):
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.delete_pedido(pedido_id)
    
# TODO
# Criar um response model com a ordem da fila
@app.get("/pedidos/fila/", tags=['Pedidos']) 
async def get_fila() -> list | None:
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.get_fila()

@app.post('/pedidos/checkout/{pedido_id}', tags=['Pedidos'], response_model = domain.Pedido)
def checkout(pedido_id: int):
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.checkout(pedido_id)

@app.get('/pedidos/{pedido_id}/verprodutos', tags=['Pedidos'], response_model = domain.ProdutoNoPedido)
def produtos_do_pedido(pedido_id: int):
    pedido_svc = services.ProdutoNoPedidoService(mysql_repo())
    return pedido_svc.produtos_no_pedido(pedido_id)

@app.post('/inserirproduto/', tags=['Pedidos'], response_model = domain.ProdutoNoPedido)
def inserir_produto_no_pedido(produto: domain.ProdutoNoPedido) -> domain.ProdutoNoPedido:
    pedido_svc = services.ProdutoNoPedidoService(mysql_repo(), mysql_repo(), mysql_repo())
    return pedido_svc.adicionar_produto(produto)

@app.post('/removerproduto/', tags=['Pedidos'])
def remover_produto_no_pedido(produto: domain.ProdutoNoPedido) -> bool:
    pedido_svc = services.ProdutoNoPedidoService(mysql_repo(), mysql_repo(), mysql_repo())
    return pedido_svc.remover_produto(produto)

