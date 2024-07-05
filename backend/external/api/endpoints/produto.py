
from external.api.SingletonFastAPI import SingletonFastAPI
from external import MySQLConnection
from fastapi import HTTPException
from adapters.controllers import ProdutoController
from common.dto import ProdutoDTO
from common.exceptions import ProdutoNotFoundException
from external.api.models import ProdutoModel
from typing import List
app = SingletonFastAPI.app().app
produto_controller = ProdutoController()

### PRODUTOS ###

## GET ##
    
@app.get("/produtos/{produto_id}", tags=['Produtos'])
async def retornar_produto_pelo_id(produto_id: int) -> ProdutoModel:
    try:
        return produto_controller.retornar_pelo_id(MySQLConnection(), produto_id)
    except ProdutoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)

@app.get("/produtos/", tags=['Produtos'])
async def listar_todos_os_produtos() -> List[ProdutoModel]:
    return produto_controller.listar_todos(MySQLConnection())

@app.get("/lanches/", tags=['Produtos'])
async def listar_lanches() -> List[ProdutoModel]:
    return produto_controller.listar_lanches(MySQLConnection())

@app.get("/acompanhamentos/", tags=['Produtos'])
async def listar_acompanhamentos() -> List[ProdutoModel]:
    return produto_controller.listar_acompanhamentos(MySQLConnection())

@app.get("/bebidas/", tags=['Produtos'])
async def listar_bebidas() -> List[ProdutoModel]:
    return produto_controller.listar_bebidas(MySQLConnection())
    
@app.get("/sobremesas/", tags=['Produtos'])
async def listar_sobremesas() -> List[ProdutoModel]:
    return produto_controller.listar_sobremesas(MySQLConnection())

## POST ##

@app.post("/produtos/", tags=['Produtos'])
async def cadastrar_produto(produto: ProdutoModel) -> ProdutoModel:
    produto_dto = ProdutoDTO(
        None,
        produto.nome,
        produto.categoria,
        produto.valor,
        produto.descricao,
        produto.ativo) 
    return produto_controller.novo(produto_dto, MySQLConnection())

## PUT ##

@app.put("/produtos/", tags=['Produtos'])
async def editar_produto(produto: ProdutoModel) -> ProdutoModel:
    try:
        return produto_controller.editar(MySQLConnection(), ProdutoDTO(
            id=produto.id,
            nome=produto.nome,
            categoria=produto.categoria,
            valor=produto.valor,
            descricao=produto.descricao,
            ativo=produto.ativo
        ))
    except ProdutoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)

## DELETE ##
    
@app.delete("/produtos/{produto_id}", tags=['Produtos'])
async def deletar_produto(produto_id: int) -> bool:
    try:
        return produto_controller.deletar(MySQLConnection(), produto_id)
    except ProdutoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    
