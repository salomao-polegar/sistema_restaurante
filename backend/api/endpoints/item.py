import domain
from api.SingletonFastAPI import SingletonFastAPI
from typing import List
import adapters.repositories as repositories
import services
from fastapi import HTTPException

app = SingletonFastAPI.app().app

def mysql_repo():
    repo = repositories.MysqlRepo()
    return repo

@app.get('/item/{pedido_id}', tags=['Itens'], response_model = List[domain.Item])
async def listar_itens(pedido_id: int) -> List[domain.Item]:
    try:
        item_svc = services.ItemService(mysql_repo(), mysql_repo(), mysql_repo())
        return item_svc.listar_itens(pedido_id)
    except services.PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    
@app.post('/item/', tags=['Itens'], response_model = domain.Item)
async def inserir_item(item: domain.Item) -> domain.Item:
    try:
        item_svc = services.ItemService(mysql_repo(), mysql_repo(), mysql_repo())
        return item_svc.inserir_item(item)
    except services.PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    except services.ProdutoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)

@app.put('/item/', tags=['Itens'], response_model = domain.Item)
async def editar_item(item: domain.Item) -> domain.Item:
    try:
        item_svc = services.ItemService(mysql_repo(), mysql_repo(), mysql_repo())
        return item_svc.editar_item(item)
    except services.PedidoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    except services.ProdutoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)

@app.delete('/item/{pedido_id}/{produto_id}', tags=['Itens'])
async def deletar_item(pedido_id: int, produto_id: int) -> bool:
    try:
        item_svc = services.ItemService(mysql_repo(), mysql_repo(), mysql_repo())
        return item_svc.deletar_item(domain.Item(produto=produto_id, pedido=pedido_id, quantidade=0))
    except services.ItemNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
