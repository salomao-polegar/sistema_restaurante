from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI

class SingletonFastAPI():
    _instance = None
    app: FastAPI

    def __init__(self):

        tags_metadata = [
            {
                "name": "Produtos",
                "description": "Você pode criar, editar, remover e retornar a lista de produtos do cardápio ou, ainda, filtrar por categorias pré-definidas.",
            },
            {
                "name": "Clientes",
                "description": "Você pode criar, editar, remover e retornar a lista de clientes.",
            },
            {
                "name": "Pedidos",
                "description": "Você pode gerenciar os pedidos do restaurante e alterar suas situações.",
            
            },
            # {
            #     "name": "Itens",
            #     "description": "Você pode gerenciar os itens dentro dos pedidos"
            # }
        ]

        self.app = FastAPI(
            title = "restauranteAPI",
            description = "API desenvolvida no contexto do Tech Challenge do curso de pós graduação em Software Architecture da FIAP",
            version='1.0.0',
            openapi_tags= tags_metadata,
            swagger_ui_parameters={"operationsSorter": "method"}
        )
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=['*'],
            allow_headers=["*"])
    
    @classmethod
    def app(self):
        if self._instance is None:
            self._instance = self()
        return self._instance