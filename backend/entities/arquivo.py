from pydantic import BaseModel


# import json

class Arquivo():
    id: int | None = None
    path: str | None = None
    
    def __init__(self,
            id: int | None = None,
            path: str | None = None):
            

        self.id = id
        self.path = path

    def __str__(self):
        return str([self.id, self.path])