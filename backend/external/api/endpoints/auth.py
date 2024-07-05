# auth
from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import jwt
from jwt.exceptions import InvalidTokenError
from external.api.SingletonFastAPI import SingletonFastAPI
from datetime import datetime, timedelta, timezone
from external.api.models import ClienteModel, BaseModel
from fastapi import HTTPException, status
from adapters.controllers import ClienteController
from external import MySQLConnection
from typing import List
import hashlib

app = SingletonFastAPI.app().app
cliente_controller = ClienteController()

SECRET_KEY = "b25dce44262703aeb2adc1972c52341d7318fcdd3d0f41deb9e018f34a45e1b7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

users_db = cliente_controller.listar_todos(MySQLConnection())
# [
#     {
#         "id": 1,
#         "cpf": null,
#         "nome": "SEM IDENTIFICAÇÃO",
#         "email": null,
#         "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
#         "telefone": null,
#         "ativo": 1
#     }
# ]

class UsuarioNaoEncontradoException(BaseException):
    def __init__(self, message = "Usuário não encontrado"):
        self.message = message
        
class Token(BaseModel):
    access_token: str
    token_type: str
    user: ClienteModel | None = None

class TokenData(BaseModel):
    username: str | None = None

# pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def verify_password(plain_password: str, hashed_password):
    pass_bytes = plain_password.encode('utf-8')
    hash = hashlib.sha256(pass_bytes).hexdigest()
    print(hash, "==", hashed_password)
    return hash == hashed_password

def get_user(db, username: str):
    for usuario in db:
        if usuario['email'] == username:
            return ClienteModel(
                id=usuario['id'], 
                cpf=usuario['cpf'],
                nome=usuario['nome'], 
                username=usuario['email'],
                email=usuario['email'], 
                telefone=usuario['telefone'],
                ativo=usuario['ativo'],
                hashed_password=usuario['hashed_password'])
    # raise UsuarioNaoEncontradoException()

def authenticate_user(users_db, username: str, password: str):
    user = get_user(users_db, username)
    
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    print(user.hashed_password)
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt



async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail = "Não foi possível validar as credenciais",
        headers = {"HTTP-Authenticate": "Bearer"}
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username:str = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(
    current_user: Annotated[ClienteModel, Depends(get_current_user)],
):
    if not current_user.ativo:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token", tags=['Users'])
async def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user: ClienteModel = authenticate_user(users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer", user=user)


@app.get("/users/me", tags=['Users'])
async def retornar_usuario_logado(
    current_user: Annotated[ClienteModel, Depends(get_current_active_user)],
):
    return current_user

@app.get("/users/me/pedidos", tags=['Users'])
async def retornar_pedidos_usuario_logado(
    current_user: Annotated[ClienteModel, Depends(get_current_active_user)],
):
    #TODO: retornar somente os pedidos do usuário
    return current_user