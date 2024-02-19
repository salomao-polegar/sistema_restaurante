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
                # "externalDocs": {
                #     "description": "Items external docs",
                #     "url": "https://fastapi.tiangolo.com/",
                # },
            },
            {
                "name": "Pedidos",
                "description": "Você pode gerenciar os pedidos do restaurante e alterar suas situações.",
            
            },
            {
                "name": "Itens",
                "description": "Você pode gerenciar os itens dentro dos pedidos"
            }
        ]

        self.app = FastAPI(
            title = "restauranteAPI",
            description = "API desenvolvida no contexto do Tech Challenge do curso de pós graduação em Software Architecture da FIAP",
            version='0.0.1',
            openapi_tags= tags_metadata
            
        )
    
    @classmethod
    def app(self):
        if self._instance is None:
            self._instance = self()
        return self._instance