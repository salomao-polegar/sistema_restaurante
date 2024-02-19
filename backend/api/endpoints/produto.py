from domain.produto import Produto
from api.SingletonFastAPI import SingletonFastAPI
from typing import List
import adapters.repositories as repositories
import services
app = SingletonFastAPI.app().app
from fastapi import HTTPException

def mysql_repo():
    repo = repositories.MysqlRepo()
    return repo

### PRODUTOS ###

@app.post("/produtos/", tags=['Produtos'], response_model=Produto)
async def inserir_produto(produto: Produto) -> Produto | None:
    try:
        produto_svc = services.ProdutoService(mysql_repo())
        return produto_svc.inserir_produto(produto)
    except services.ProdutoAlreadyExistsException as e:
        raise HTTPException(status_code=404, detail = e.message)


@app.get("/produtos/{produto_id}", tags=['Produtos'], response_model=Produto)
async def retornar_produto(produto_id) -> Produto | None:
    try:
        produto_svc = services.ProdutoService(mysql_repo())
        return produto_svc.retornar_produto(produto_id)
    except services.ProdutoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)

@app.get("/produtos/", tags=['Produtos'], response_model=List[Produto])
async def listar_produtos() -> List[Produto] | None:
    produto_svc = services.ProdutoService(mysql_repo())
    return produto_svc.listar_produtos()

@app.get("/lanches/", tags=['Produtos'], response_model=List[Produto])
async def listar_lanches():
    produto_svc = services.ProdutoService(mysql_repo())
    return produto_svc.listar_lanches()  

@app.get("/acompanhamentos/", tags=['Produtos'], response_model=List[Produto])
async def listar_acompanhamentos():
    produto_svc = services.ProdutoService(mysql_repo())
    return produto_svc.listar_acompanhamentos()

@app.get("/bebidas/", tags=['Produtos'], response_model=List[Produto])
async def listar_bebidas():
    produto_svc = services.ProdutoService(mysql_repo())
    return produto_svc.listar_bebidas()
    
@app.get("/sobremesas/", tags=['Produtos'], response_model=List[Produto])
async def listar_sobremesas():
    produto_svc = services.ProdutoService(mysql_repo())
    return produto_svc.listar_sobremesas()

@app.put("/produtos/", tags=['Produtos'], response_model=Produto)
async def editar_produto(produto: Produto) -> Produto | None:
    try:
        produto_svc = services.ProdutoService(mysql_repo())
        return produto_svc.editar_produto(produto)
    except services.ProdutoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)

@app.delete("/produtos/{produto_id}", tags=['Produtos'])
async def deletar_produto(produto_id: int) -> bool:
    try:
        produto_svc = services.ProdutoService(mysql_repo())
        return produto_svc.deletar_produto(produto_id)
    except services.ProdutoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)
    
