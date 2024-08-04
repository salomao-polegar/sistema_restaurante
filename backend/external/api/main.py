from external.api.SingletonFastAPI import SingletonFastAPI
# from external.api.endpoints.auth import *
from external.api.endpoints.cliente import *
from external.api.endpoints.produto import *
from external.api.endpoints.pedido import *
# from external.api.endpoints.item import *
from external.api.endpoints.files import *
from external.api.endpoints.webhook_pedidos import *
from fastapi.responses import RedirectResponse

app = SingletonFastAPI.app().app

@app.get("/")
def read_root():
    return RedirectResponse('/redoc')





