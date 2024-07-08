from external.api.SingletonFastAPI import SingletonFastAPI
from adapters.controllers import ClienteController, PedidoController
from external import MySQLConnection
from common.dto import ClienteDTO
from common.exceptions import ClienteNotFoundException, ClienteAlreadyExistsException, MysqlConnectionException
from fastapi import HTTPException
from external.api.models import ClienteModel, PedidoModel
from typing import List

app = SingletonFastAPI.app().app
cliente_controller = ClienteController()
pedidos_controller = PedidoController()
### CLIENTES ###

## GET ##

@app.get("/clientes/", tags=['Clientes'])
async def listar_todos_os_clientes() -> List[ClienteModel]:
    try:
        return cliente_controller.listar_todos(MySQLConnection())
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)

@app.get("/clientes/{cliente_id}", tags=['Clientes'])
async def retornar_cliente_pelo_id(cliente_id: int) -> ClienteModel:
    try:
        return cliente_controller.retornar_pelo_id(MySQLConnection(), cliente_id)
    except ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)
    

@app.get("/clientes/{cliente_id}/pedidos/", tags=['Clientes'])
async def retornar_pedidos_do_ciente(cliente_id: int) -> List[PedidoModel]:
    try:
        return pedidos_controller.listar_por_cliente_id(MySQLConnection(), cliente_id)
    except ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)


## POST ##
    
@app.post("/clientes/", tags=['Clientes'])
async def cadastrar_cliente(cliente: ClienteModel) -> ClienteModel:
    # pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    try:
        cliente = ClienteDTO(None, cliente.cpf, cliente.nome, cliente.email, cliente.hashed_password, cliente.telefone, cliente.ativo)
        print(cliente)
        return cliente_controller.novo(cliente, MySQLConnection())
    except ClienteAlreadyExistsException as e:
        raise HTTPException(status_code=409, detail=e.message)
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)

## PUT ##

@app.put("/clientes/", tags=['Clientes'])
async def editar_cliente(cliente: ClienteModel) -> ClienteModel:
    try:
        return cliente_controller.editar(MySQLConnection(), ClienteDTO(
            id=cliente.id,
            cpf=cliente.cpf,
            nome=cliente.nome,
            email=cliente.email,
            hashed_password=cliente.hashed_password,
            telefone=cliente.telefone,
            ativo=cliente.ativo
        ))        
    except ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)

## DELETE ##

@app.delete("/clientes/{cliente_id}", tags=['Clientes'])
async def deletar_cliente(cliente_id: int) -> bool:
    try:
        return cliente_controller.deletar(MySQLConnection(), cliente_id)
    except ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)
    except MysqlConnectionException as e:
        raise HTTPException(status_code=503, detail= e.message)