# from app.Entidades.Pedido import Pedido
# from app.Entidades.Produto import Produto
# from app.mysql_connection import get_connection
from api.SingletonFastAPI import SingletonFastAPI
from api.endpoints.cliente import *
from api.endpoints.produto import *
from api.endpoints.pedido import *
from api.endpoints.item import *
from fastapi.responses import RedirectResponse

app = SingletonFastAPI.app().app

@app.get("/")
def read_root():
    return RedirectResponse('/redoc')



