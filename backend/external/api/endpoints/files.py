
from external.api.SingletonFastAPI import SingletonFastAPI
from fastapi.responses import FileResponse
from adapters.controllers import ArquivoController
from common.exceptions import ArquivoNotFoundException
from fastapi import HTTPException, File
from starlette.responses import StreamingResponse
from external import MySQLConnection
import uuid
from pydantic import Base64Str, BaseModel
import base64

app = SingletonFastAPI.app().app
arquivosController = ArquivoController()

@app.get('/foto/{id}', tags=['Arquivos'])
async def retornar_foto(id: str) -> FileResponse:
    try:
        return FileResponse(arquivosController.retornar_caminho_pelo_id(MySQLConnection(), id))
    except ArquivoNotFoundException as e:
        raise HTTPException(status_code=404, detail = e.message)

class FotoModel(BaseModel):
    img_bytes: str

@app.post('/foto/', tags=['Arquivos'])
async def adicionar_foto(img_bytes: FotoModel) -> StreamingResponse:
    
    img = base64.b64decode(img_bytes.img_bytes)
    path = f'/media/imagens/${str(uuid.uuid4())}'

    with open(path, 'wb') as file:
        file.write(img)
    
    try:
        return arquivosController.adicionar_foto(MySQLConnection(), path)
    except Exception as e:
        raise HTTPException(status_code=404, detail = e)
    