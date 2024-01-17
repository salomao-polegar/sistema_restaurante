from fastapi import FastAPI

class SingletonFastAPI():
    _instance = None
    app: FastAPI

    def __init__(self):

        self.app = FastAPI()
    
    @classmethod
    def app(self):
        if self._instance is None:
            self._instance = self()
        return self._instance