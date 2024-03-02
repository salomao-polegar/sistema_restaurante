# from app.Entidades.Pedido import Pedido
# from app.Entidades.Produto import Produto
# from app.mysql_connection import get_connection
from external.api.SingletonFastAPI import SingletonFastAPI
from external.api.endpoints.cliente import *
from external.api.endpoints.produto import *
from external.api.endpoints.pedido import *
from external.api.endpoints.item import *
from fastapi.responses import RedirectResponse

app = SingletonFastAPI.app().app

@app.get("/")
def read_root():
    return RedirectResponse('/redoc')



