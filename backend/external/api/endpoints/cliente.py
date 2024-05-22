from external.api.SingletonFastAPI import SingletonFastAPI
from adapters.controllers import ClienteController
from external import MySQLConnection
from common.dto import ClienteDTO
from common.exceptions import ClienteNotFoundException, ClienteAlreadyExistsException
from fastapi import HTTPException
from external.api.models import ClienteModel
from pydantic import BaseModel

app = SingletonFastAPI.app().app
cliente_controller = ClienteController()

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
    
## POST ##
    
@app.post("/clientes/", tags=['Clientes'])
async def inserir_cliente(clienteDTO: ClienteModel):
    try:
        cliente = ClienteDTO(None, clienteDTO.cpf, clienteDTO.nome, clienteDTO.email, clienteDTO.telefone, clienteDTO.ativo)
        
        return cliente_controller.novo(cliente, MySQLConnection())
    except ClienteAlreadyExistsException as e:
        raise HTTPException(status_code=404, detail=e.message)

## PUT ##

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

## DELETE ##

@app.delete("/clientes/{cliente_id}", tags=['Clientes'])
async def deletar_cliente(cliente_id: int) -> bool:
    try:
        return cliente_controller.deletar(MySQLConnection(), cliente_id)
    except ClienteNotFoundException as e:
        raise HTTPException(status_code=404, detail=e.message)


class LoginModel (BaseModel):
    email:str
    senha:str

class AuthResponse (BaseModel):
    auth: bool
    token: str
    rota:str

## AUTH ##
@app.post("/auth/login", tags=['Clientes'])
async def login(loginDTO: LoginModel) -> AuthResponse:
    auth = loginDTO.email=="admin" and loginDTO.senha=="admin"
    if auth == False: return False
    return {
        "auth":True,
        "token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjQ4ZjU4OWIyLTljNmYtNDhjZC1iYTVjLWQ1OGM2OWYyYmNiOCIsInJvbGUiOiJQQUNJRU5URSIsImlhdCI6MTY4MTkxMjY0MSwiZXhwIjoxNjgxOTk5MDQxfQ.FpL09UPBn7_4e9nx84QGh7Ekut14gdQl7Acp32KyMI",
        "rota":"/paciente"
    }
