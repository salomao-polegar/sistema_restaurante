from domain.cliente import Cliente
from api.SingletonFastAPI import SingletonFastAPI
from typing import List
import adapters.repositories as repositories
import services
from fastapi import HTTPException
app = SingletonFastAPI.app().app

def mysql_repo():
    repo = repositories.MysqlRepo()
    return repo

### CLIENTES ###

@app.post("/clientes/", tags=['Clientes'], response_model=Cliente)
async def inserir_cliente(cliente: Cliente) -> Cliente | None:
    try:
        cliente_svc = services.ClienteService(mysql_repo())
        return cliente_svc.inserir_cliente(cliente)
    except services.ClienteAlreadyExistsException as e:
        raise HTTPException(status_code=404, detail=e.message)

@app.get("/clientes/{cliente_id}", tags=['Clientes'], response_model=Cliente)
async def retornar_cliente(cliente_id: int) -> Cliente | None:
    try: 
        cliente_svc = services.ClienteService(mysql_repo())
        return cliente_svc.retornar_cliente_pelo_id(cliente_id)
    except services.ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)

@app.get("/clientes/", tags=['Clientes'], response_model=List[Cliente])
async def listar_clientes() -> List[Cliente] | None:
    cliente_svc = services.ClienteService(mysql_repo())
    return cliente_svc.listar_clientes()

@app.put("/clientes/", tags=['Clientes'], response_model=Cliente)
async def editar_cliente(cliente: Cliente) -> Cliente | None:
    try:
        cliente_svc = services.ClienteService(mysql_repo())
        return cliente_svc.editar_cliente(cliente)
    except services.ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)

@app.delete("/clientes/{cliente_id}", tags=['Clientes'])
async def deletar_cliente(cliente_id: int) -> bool:
    try:
        cliente_svc = services.ClienteService(mysql_repo())
        return cliente_svc.deletar_cliente(cliente_id)
    except services.ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)