
from external.api.SingletonFastAPI import SingletonFastAPI
from typing import List
from external import MySQLConnection, MercadoPagoConnection
from fastapi import HTTPException
from adapters.controllers import PedidoController
from common.dto import PedidoDTO
from common.exceptions import PedidoNotFoundException, ClienteNotFoundException, ProdutoNotFoundException, PedidoEditadoComItensException, MysqlConnectionException
from external.api.models import PedidoCheckoutModel, PedidoModel, PedidoEditarModel
from typing import Dict

app = SingletonFastAPI.app().app
pedido_controller = PedidoController()

### PEDIDOS ###

## GET ##

@app.get("/pedidos/{pedido_id}", tags=['Pedidos'])
async def retornar_pedido_pelo_id(pedido_id: int) -> PedidoModel | None:
    try:
        return pedido_controller.retornar_pelo_id(MySQLConnection(), pedido_id)
    except PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)

@app.get("/pedidos/", tags=['Pedidos'])
# async def listar_pedidos(cliente: ClienteModel = None) -> List[PedidoModel]:
async def listar_pedidos() -> List[PedidoModel]:
    try:
        return pedido_controller.listar_todos(MySQLConnection())
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)

@app.get("/pedidos/recebidos/", tags=['Pedidos'])
async def listar_pedidos_recebidos() -> List[PedidoModel]:
    try:
        return pedido_controller.listar_pedidos_recebidos(MySQLConnection())
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)

@app.get("/pedidos/empreparacao/", tags=['Pedidos'])
async def listar_pedidos_em_preparacao() -> List[PedidoModel]:
    try:
        return pedido_controller.listar_pedidos_em_preparacao(MySQLConnection())
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)

@app.get("/pedidos/prontos/", tags=['Pedidos'])
async def listar_pedidos_prontos() -> List[PedidoModel]:
    try:
        return pedido_controller.listar_pedidos_prontos(MySQLConnection())
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)

@app.get("/pedidos/finalizados/", tags=['Pedidos'])
async def listar_pedidos_finalizados() -> List[PedidoModel]:
    try:
        return pedido_controller.listar_pedidos_finalizados(MySQLConnection())
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)
    
@app.get("/pedidos/naofinalizados/", tags=['Pedidos'])
async def listar_pedidos_nao_finalizados():
    try:
        return pedido_controller.listar_pedidos_nao_finalizados(MySQLConnection())
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)

@app.get("/pedidos/fila/", tags=['Pedidos']) 
async def listar_fila() -> List[PedidoModel]:
    try:
        return pedido_controller.listar_fila(MySQLConnection())
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)

@app.get('/pedidos/{pedido_id}/status_pagamento/', tags=['Pedidos'])
async def retorna_status_pagamento(pedido_id: int) -> str:
    try:
        return pedido_controller.retorna_status_pagamento(pedido_id, MySQLConnection())
        
    except PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)
    
## POST ##

# @app.post("/pedidos/", tags=['Pedidos'])
# async def inserir_pedido(pedido: PedidoModel) -> PedidoModel:
#     try:
#         pedido_dto = PedidoDTO(
#             id=None,
#             status_pedido=pedido.status_pedido,
#             cliente=pedido.cliente,
#             datahora_recebido=pedido.datahora_recebido,
#             datahora_preparacao=pedido.datahora_preparacao,
#             datahora_pronto=pedido.datahora_pronto,
#             datahora_finalizado=pedido.datahora_finalizado,
#             status_pagamento=pedido.status_pagamento,
#             valor_total=pedido.valor_total)
        
#         return pedido_controller.novo(pedido_dto, MySQLConnection())
#     except MysqlConnectionException as e:
#         raise HTTPException(status_code=503, detail= e.message)
#     except ClienteNotFoundException as e:
#         raise HTTPException(status_code=503, detail= e.message)

@app.post('/pedidos/checkout/', tags=['Pedidos'])
async def checkout(pedido: PedidoCheckoutModel) -> PedidoModel:
    try:
        pedido_inserido = pedido_controller.checkout(pedido, MySQLConnection(), MercadoPagoConnection())
        # print(repr(pedido_inserido))
        return pedido_inserido
        
    except ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    
    except ProdutoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)

## PUT ##

@app.put("/pedidos/", tags=['Pedidos'])
async def editar_pedido(pedido: PedidoEditarModel) -> PedidoModel:
    try:
        
        return pedido_controller.editar(MySQLConnection(), PedidoDTO(
        id=pedido.id,
        status_pedido=pedido.status_pedido,
        cliente=pedido.cliente,
        datahora_recebido=pedido.datahora_recebido,
        datahora_preparacao=pedido.datahora_preparacao,
        datahora_pronto=pedido.datahora_pronto,
        datahora_finalizado=pedido.datahora_finalizado,
        id_pagamento=pedido.status_pagamento))
    except PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    except ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    except PedidoEditadoComItensException as e:
        raise HTTPException(status_code=422, detail = e.message)
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)
    
# @app.put("/pedidos/status/", tags=['Pedidos'])
# async def editar_pedido(pedido: PedidoAtualizarStatusModel) -> PedidoModel:
#     try:
        
#         return pedido_controller.editar_status(MySQLConnection(), PedidoAtualizarStatusDTO(
#         id=pedido.id,
#         status_pedido=pedido.status_pedido))
#     except PedidoNotFoundException as e:
#         raise HTTPException(status_code=404, detail = e.message)
#     except ClienteNotFoundException as e:
#         raise HTTPException(status_code=404, detail = e.message)
#     except PedidoEditadoComItensException as e:
#         raise HTTPException(status_code=422, detail = e.message)
#     except MysqlConnectionException as e:
#         raise HTTPException(status_code=503, detail= e.message)
    
    
## DELETE ##

@app.delete("/pedidos/{pedido_id}", tags=['Pedidos'])
async def deletar_pedido(pedido_id: int) -> bool:
    try:
        return pedido_controller.deletar(MySQLConnection(), pedido_id)
    except PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)
    

    

    








