import domain
from fastapi import HTTPException
from api.SingletonFastAPI import SingletonFastAPI
from typing import List
import adapters.repositories as repositories
import services
app = SingletonFastAPI.app().app

def mysql_repo():
    repo = repositories.MysqlRepo()
    return repo

### PEDIDOS ###

@app.post("/pedidos/", tags=['Pedidos'], response_model=domain.Pedido)
async def inserir_pedido(pedido: domain.Pedido) -> domain.Pedido | None:
    try:
        pedido_svc = services.PedidoService(mysql_repo())
        return pedido_svc.inserir_pedido(pedido)
    except services.PedidoAlreadyExistsException as e:
        raise HTTPException(status_code=404, detail = e.message)

@app.get("/pedidos/{pedido_id}", tags=['Pedidos'], response_model=domain.Pedido)
async def retornar_pedido(pedido_id: int) -> domain.Pedido | None:
    try:
        pedido_svc = services.PedidoService(mysql_repo())
        return pedido_svc.retornar_pedido(pedido_id)
    except services.PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)

@app.get("/pedidos/", tags=['Pedidos'], response_model=List[domain.Pedido])
async def listar_pedidos() -> List[domain.Pedido] | None:
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.listar_pedidos()

@app.get("/pedidos/recebidos/", tags=['Pedidos'], response_model=List[domain.Pedido])
async def listar_pedidos_recebidos():
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.listar_pedidos_recebidos()  

@app.get("/pedidos/empreparacao/", tags=['Pedidos'], response_model=List[domain.Pedido])
async def listar_pedidos_em_preparacao():
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.listar_pedidos_em_preparacao()

@app.get("/pedidos/finalizados/", tags=['Pedidos'], response_model=List[domain.Pedido])
async def listar_pedidos_finalizados():
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.listar_pedidos_finalizados()
    
@app.get("/pedidos/naofinalizados/", tags=['Pedidos'], response_model=List[domain.Pedido])
async def listar_pedidos_nao_finalizados():
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.listar_pedidos_nao_finalizados()

@app.put("/pedidos/", tags=['Pedidos'], response_model=domain.Pedido)
async def editar_pedido(pedido: domain.Pedido) -> domain.Pedido | None:
    try:
        pedido_svc = services.PedidoService(mysql_repo())
        return pedido_svc.editar_pedido(pedido)
    except services.PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)

@app.delete("/pedidos/{pedido_id}", tags=['Pedidos'])
async def deletar_pedido(pedido_id: int):
    try:
        pedido_svc = services.PedidoService(mysql_repo())
        return pedido_svc.deletar_pedido(pedido_id)
    except services.PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    
@app.get("/pedidos/fila/", tags=['Pedidos']) 
async def listar_fila() -> list | None:
    pedido_svc = services.PedidoService(mysql_repo())
    return pedido_svc.listar_fila()

@app.post('/pedidos/checkout/{pedido_id}', tags=['Pedidos'], response_model = domain.Pedido)
async def checkout(pedido_id: int) -> domain.Pedido:
    try:
        pedido_svc = services.PedidoService(mysql_repo())
        return pedido_svc.checkout(pedido_id)
    except services.PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    
@app.get('/pedidos/status_pagamento/{pedido_id}', tags=['Pedidos'])
async def retorna_status_pagamento(pedido_id: int) -> str:
    try:
        pedido_svc = services.PedidoService(mysql_repo())
        return pedido_svc.retorna_status_pagamento(pedido_id)
    except services.PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)







