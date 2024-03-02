
from external.api.SingletonFastAPI import SingletonFastAPI
from typing import List
from external import MySQLConnection
from fastapi import HTTPException
from pydantic import BaseModel
from adapters.controllers import PedidoController
from common.dto import PedidoDTO
from common.exceptions import PedidoNotFoundException
from datetime import datetime

app = SingletonFastAPI.app().app
pedido_controller = PedidoController()

class PedidoModel(BaseModel):
    id: int | None = None
    status_pedido: int | None = None
    cliente: int
    datahora_recebido: datetime | None = None
    datahora_preparacao: datetime | None = None
    datahora_pronto: datetime | None = None
    datahora_finalizado: datetime | None = None
    status_pagamento: int | None = None

### PEDIDOS ###

@app.post("/pedidos/", tags=['Pedidos'])
async def inserir_pedido(pedido: PedidoModel):
    pedido_dto = PedidoDTO(
        None,
        pedido.status_pedido,
        pedido.cliente,
        pedido.datahora_recebido,
        pedido.datahora_preparacao,
        pedido.datahora_pronto,
        pedido.datahora_finalizado,
        pedido.status_pagamento)
     
    return pedido_controller.novo(pedido_dto, MySQLConnection())

@app.get("/pedidos/{pedido_id}", tags=['Pedidos'])
async def retornar_pedido(pedido_id: int):
    try:
        return pedido_controller.retornar_pelo_id(MySQLConnection(), pedido_id)
    except PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)

@app.get("/pedidos/", tags=['Pedidos'])
async def listar_pedidos() -> List[PedidoModel] | None:
    return pedido_controller.listar_todos(MySQLConnection())

@app.get("/pedidos/recebidos/", tags=['Pedidos'])
async def listar_pedidos_recebidos():
    return pedido_controller.listar_pedidos_recebidos(MySQLConnection())

@app.get("/pedidos/empreparacao/", tags=['Pedidos'])
async def listar_pedidos_em_preparacao():
    return pedido_controller.listar_pedidos_em_preparacao(MySQLConnection())

@app.get("/pedidos/finalizados/", tags=['Pedidos'])
async def listar_pedidos_finalizados():
    return pedido_controller.listar_pedidos_finalizados(MySQLConnection())
    
@app.get("/pedidos/naofinalizados/", tags=['Pedidos'])
async def listar_pedidos_nao_finalizados():
    return pedido_controller.listar_pedidos_nao_finalizados(MySQLConnection())

@app.put("/pedidos/", tags=['Pedidos'])
async def editar_pedido(pedido: PedidoModel):
    try:
        return pedido_controller.editar(MySQLConnection(), PedidoDTO(
        pedido.id,
        pedido.status_pedido,
        pedido.cliente,
        pedido.datahora_recebido,
        pedido.datahora_preparacao,
        pedido.datahora_pronto,
        pedido.datahora_finalizado,
        pedido.status_pagamento))
    except PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    

@app.delete("/pedidos/{pedido_id}", tags=['Pedidos'])
async def deletar_pedido(pedido_id: int):
    try:
        return pedido_controller.deletar(pedido_id)
    except PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    
@app.get("/pedidos/fila/", tags=['Pedidos']) 
async def listar_fila():
    return pedido_controller.listar_fila(MySQLConnection())
    
@app.post('/pedidos/checkout/{pedido_id}', tags=['Pedidos'])
async def checkout(pedido_id: int):
    try:
        return pedido_controller.checkout(pedido_id, MySQLConnection())
        
    except PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    
@app.get('/pedidos/status_pagamento/{pedido_id}', tags=['Pedidos'])
async def retorna_status_pagamento(pedido_id: int) -> str:
    try:
        return pedido_controller.retorna_status_pagamento(pedido_id, MySQLConnection())
        
    except PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)







