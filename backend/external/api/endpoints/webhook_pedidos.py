
from external.api.SingletonFastAPI import SingletonFastAPI
from external import MySQLConnection
from external.api.models import PedidoModel
from fastapi import HTTPException, Response, status
from adapters.controllers import PedidoController
from common.dto import ProdutoDTO
from common.exceptions import PedidoNotFoundException
from pydantic import BaseModel

app = SingletonFastAPI.app().app
pedido_controller = PedidoController()

### WEBHOOK PARA ATUALIZAÇÃO DO STATUS DO PAGAMENTO

class webhookModel(BaseModel):
    id: str
    type: str # "payment",
    date_created: str # "2015-03-25T10:04:58.396-04:00",
    user_id: int # 44444,
    api_version: str #"v1",
    action: str # "payment.created",


@app.post('/pedidos/status_pagamento/', tags=['Pedidos'])
async def webhook_status_pagamento(status_pagamento: webhookModel) -> PedidoModel:
    try:
        return pedido_controller.atualiza_status_pagamento(status_pagamento, MySQLConnection())
    except PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)