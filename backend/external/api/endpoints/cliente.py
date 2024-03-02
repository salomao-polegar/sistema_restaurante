from external.api.SingletonFastAPI import SingletonFastAPI
from typing import List
from adapters.controllers import ClienteController
from external import MySQLConnection
from common.interfaces import DbConnection
from common.dto import ClienteDTO
from common.exceptions import ClienteNotFoundException, ClienteAlreadyExistsException
from fastapi import HTTPException
from pydantic import BaseModel

app = SingletonFastAPI.app().app
cliente_controller = ClienteController()

### CLIENTES ###
class ClienteModel(BaseModel):
    id: int | None = None
    cpf: str | None = None
    nome: str | None = None
    email: str | None = None
    telefone: str | None = None
    ativo: bool = True

@app.get("/clientes/", tags=['Clientes'])
async def listar_clientes():
    return cliente_controller.listar_todos(MySQLConnection())

@app.post("/clientes/", tags=['Clientes'])
async def inserir_cliente(clienteDTO: ClienteModel):
    try:
        cliente = ClienteDTO(None, clienteDTO.cpf, clienteDTO.nome, clienteDTO.email, clienteDTO.telefone, clienteDTO.ativo)
        
        return cliente_controller.novo(cliente, MySQLConnection())
    except ClienteAlreadyExistsException as e:
        raise HTTPException(status_code=404, detail=e.message)

@app.get("/clientes/{cliente_id}", tags=['Clientes'])
async def retornar_cliente(cliente_id: int):
    try:
        return cliente_controller.retornar_pelo_id(MySQLConnection(), cliente_id)
    except ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)

@app.put("/clientes/", tags=['Clientes'])
async def editar_cliente(cliente: ClienteModel) -> bool:
    try:
        return cliente_controller.editar(MySQLConnection(), ClienteDTO(
            id=cliente.id,
            cpf=cliente.cpf,
            nome=cliente.nome,
            email=cliente.email,
            telefone=cliente.telefone,
            ativo=cliente.ativo
        ))        
    except ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)

@app.delete("/clientes/{cliente_id}", tags=['Clientes'])
async def deletar_cliente(cliente_id: int) -> bool:
    try:
        return cliente_controller.deletar(MySQLConnection(), cliente_id)
    except ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


