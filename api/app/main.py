from app.Entidades.Pedido import Pedido
from app.Entidades.Produto import Produto
from app.mysql_connection import get_connection
from app.SingletonFastAPI import SingletonFastAPI
from app.endpoints.cliente import *
from app.endpoints.produto import *
from app.endpoints.pedido import *


app = SingletonFastAPI.app().app



@app.get("/")
def read_root():
    return {"Hello": "World"}



