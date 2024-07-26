from locust import HttpUser, between, task

class WebsiteUser(HttpUser):
    wait_time = between(1, 10)
    
    # def on_start(self):
    #     self.client.post("/login", {
    #         "username": "test_user",
    #         "password": ""
    #     })
    
    
    @task
    def pedidos(self):
        self.client.get("/pedidos/")
    
    @task
    def clientes(self):
        self.client.get("/clientes/")
    
    @task
    def produtos(self):
        self.client.get("/produtos/")
        