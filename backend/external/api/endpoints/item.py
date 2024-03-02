
from external.api.SingletonFastAPI import SingletonFastAPI
from typing import List
from external import MySQLConnection
from fastapi import HTTPException
from pydantic import BaseModel
from adapters.controllers import ItemController
from common.dto import ItemDTO, ProdutoDTO, PedidoDTO
from common.exceptions import ItemNotFoundException, ProdutoNotFoundException, PedidoNotFoundException
from .pedido import PedidoModel
from .produto import ProdutoModel

app = SingletonFastAPI.app().app
item_controller = ItemController()

class ItemModel(BaseModel):
    produto: int
    pedido: int
    quantidade: int = 0
    descricao: str | None
    
@app.get('/item/{pedido_id}', tags=['Itens'])
async def listar_itens(pedido_id: int):
    try:
        return item_controller.listar_itens(MySQLConnection(), pedido_id)
    except ItemNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    
@app.post('/item/', tags=['Itens'])
async def inserir_item(item_dto: ItemModel):
    try:
        return item_controller.novo(item_dto, MySQLConnection())
    except ItemNotFoundException | ProdutoNotFoundException | PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)

@app.put('/item/', tags=['Itens'])
async def editar_item(item: ItemModel):
    try:
        return item_controller.editar(MySQLConnection(), item)
    except ItemNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    
@app.delete('/item/{pedido_id}/{produto_id}')
async def deletar_item(item: ItemModel) -> bool:
    try:
        return item_controller.deletar(MySQLConnection(), 
                                       ItemDTO(
                                           pedido=item.pedido,
                                           produto=item.produto))
        
    except ItemNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
