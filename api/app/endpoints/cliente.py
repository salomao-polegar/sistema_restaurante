from domain.cliente import Cliente
from app.SingletonFastAPI import SingletonFastAPI
from typing import List
import adapters.repositories as repositories
import services
app = SingletonFastAPI.app().app

def mysql_repo():
    repo = repositories.MysqlRepo()
    return repo

### CLIENTES ###

@app.post("/clientes/", tags=['Clientes'], response_model=Cliente)
async def salva_cliente(cliente: Cliente) -> Cliente | None:
    cliente_svc = services.ClienteService(mysql_repo())
    print('clientes')
    return cliente_svc.insert_cliente(cliente)

@app.get("/clientes/{cliente_id}", tags=['Clientes'], response_model=Cliente)
def get_cliente(cliente_id: int) -> Cliente | None:
    cliente_svc = services.ClienteService(mysql_repo())
    return cliente_svc.get_cliente(cliente_id)

@app.get("/clientes/", tags=['Clientes'], response_model=List[Cliente])
async def get_clientes() -> List[Cliente] | None:
    cliente_svc = services.ClienteService(mysql_repo())
    return cliente_svc.get_todos_clientes()

@app.put("/clientes/", tags=['Clientes'], response_model=Cliente)
async def edita_cliente(cliente: Cliente) -> Cliente | None:
    cliente_svc = services.ClienteService(mysql_repo())
    return cliente_svc.edita_cliente(cliente)

@app.delete("/clientes/", tags=['Clientes'])
def delete_cliente(cliente_id: int):
    cliente_svc = services.ClienteService(mysql_repo())
    return cliente_svc.delete_cliente(cliente_id)