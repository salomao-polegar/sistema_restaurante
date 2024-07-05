from external.api.SingletonFastAPI import SingletonFastAPI
from adapters.controllers import ClienteController, PedidoController
from external import MySQLConnection
from common.dto import ClienteDTO
from common.exceptions import ClienteNotFoundException, ClienteAlreadyExistsException
from fastapi import HTTPException
from external.api.models import ClienteModel
from passlib.context import CryptContext
from pydantic import BaseModel

app = SingletonFastAPI.app().app
cliente_controller = ClienteController()
pedidos_controller = PedidoController()
### CLIENTES ###

## GET ##

@app.get("/clientes/", tags=['Clientes'])
async def listar_clientes():
    return cliente_controller.listar_todos(MySQLConnection())

@app.get("/clientes/{cliente_id}", tags=['Clientes'])
async def retornar_cliente(cliente_id: int):
    try:
        return cliente_controller.retornar_pelo_id(MySQLConnection(), cliente_id)
    except ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)
    

@app.get("/clientes/{cliente_id}/pedidos/")
async def retornar_pedidos_pelo_ciente(cliente_id: int):
    try:
        return pedidos_controller.listar_por_cliente_id(MySQLConnection(), cliente_id)
    except ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


## POST ##
    
@app.post("/clientes/", tags=['Clientes'])
async def inserir_cliente(cliente: ClienteModel):
    # pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

    try:
        cliente = ClienteDTO(None, cliente.cpf, cliente.nome, cliente.email, cliente.hashed_password, cliente.telefone, cliente.ativo)
        print(cliente)
        return cliente_controller.novo(cliente, MySQLConnection())
    except ClienteAlreadyExistsException as e:
        raise HTTPException(status_code=409, detail=e.message)

## PUT ##

@app.put("/clientes/", tags=['Clientes'])
async def editar_cliente(cliente: ClienteModel) -> bool:
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

## DELETE ##

@app.delete("/clientes/{cliente_id}", tags=['Clientes'])
async def deletar_cliente(cliente_id: int) -> bool:
    try:
        return cliente_controller.deletar(MySQLConnection(), cliente_id)
    except ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)