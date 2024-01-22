from domain.produto import Produto
from app.SingletonFastAPI import SingletonFastAPI
from typing import List
import adapters.repositories as repositories
import services
app = SingletonFastAPI.app().app

def mysql_repo():
    repo = repositories.MysqlRepo()
    return repo

### PRODUTOS ###

@app.post("/produtos/", tags=['Produtos'], response_model=Produto)
async def salva_produto(produto: Produto) -> Produto | None:
    produto_svc = services.ProdutoService(mysql_repo())
    return produto_svc.insert_produto(produto)

@app.get("/produtos/{produto_id}", tags=['Produtos'], response_model=Produto)
def get_produto(produto_id: int) -> Produto | None:
    produto_svc = services.ProdutoService(mysql_repo())
    return produto_svc.get_produto(produto_id)

@app.get("/produtos/", tags=['Produtos'], response_model=List[Produto])
async def get_produtos() -> List[Produto] | None:
    produto_svc = services.ProdutoService(mysql_repo())
    return produto_svc.get_todos_produtos()

@app.get("/lanches/", tags=['Produtos'], response_model=List[Produto])
async def get_lanche():
    produto_svc = services.ProdutoService(mysql_repo())
    return produto_svc.get_lanches()  

@app.get("/acompanhamentos/", tags=['Produtos'], response_model=List[Produto])
async def get_acompanhamentos():
    produto_svc = services.ProdutoService(mysql_repo())
    return produto_svc.get_acompanhamentos()

@app.get("/bebidas/", tags=['Produtos'], response_model=List[Produto])
async def get_bebidas():
    produto_svc = services.ProdutoService(mysql_repo())
    return produto_svc.get_bebidas()
    
@app.get("/sobremesas/", tags=['Produtos'], response_model=List[Produto])
async def get_sobremesas():
    produto_svc = services.ProdutoService(mysql_repo())
    return produto_svc.get_sobremesas()

@app.put("/produtos/", tags=['Produtos'], response_model=Produto)
async def edita_produto(produto: Produto) -> Produto | None:
    produto_svc = services.ProdutoService(mysql_repo())
    return produto_svc.edita_produto(produto)

@app.delete("/produtos/{produto_id}", tags=['Produtos'])
def delete_produto(produto_id: int):
    produto_svc = services.ProdutoService(mysql_repo())
    return produto_svc.delete_produto(produto_id)
    
