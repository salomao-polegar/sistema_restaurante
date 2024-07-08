from entities import Cliente
from common.interfaces.dbconnection import DbConnection
from common.interfaces.gateways import ClienteGatewayInterface
from common.tipos import ParametroBd
from common.dto import ClienteDTO
from typing import List

class ClienteGateway (ClienteGatewayInterface):
    repositorio: DbConnection
    nomeTabela = "clientes"

    def __init__(self, repositorio: DbConnection):
        self.repositorio = repositorio
    
    def listar_todos(self) -> List[Cliente]:
        result = self.repositorio.buscar_todas(self.nomeTabela, None)

        if result == None: return None
        else:
            returnData: List[Cliente] = []
            for c in result:
                returnData.append(Cliente(id = c['id'], cpf = c['cpf'], nome = c['nome'], email= c['email'], hashed_password = c['hashed_password'], telefone=c['telefone'], ativo=c['ativo']))
            return returnData
        
    def novo(self, cliente_dto: ClienteDTO) -> Cliente:
        parametros: List[ParametroBd] = []
        parametros.append(ParametroBd(campo = "cpf", valor = cliente_dto.cpf))
        parametros.append(ParametroBd(campo = "nome", valor = cliente_dto.nome))
        parametros.append(ParametroBd(campo = "email", valor = cliente_dto.email))
        parametros.append(ParametroBd(campo = "hashed_password", valor = cliente_dto.hashed_password))
        parametros.append(ParametroBd(campo = "telefone", valor = cliente_dto.telefone))
        parametros.append(ParametroBd(campo = "ativo", valor = cliente_dto.ativo))
        
        self.repositorio.inserir(self.nomeTabela, parametros)
    
        id_inserido = self.repositorio.retorna_ultimo_id(self.nomeTabela)
        
        return Cliente(
                    id = id_inserido,
                    nome = cliente_dto.nome,
                    cpf= cliente_dto.cpf,
                    email=cliente_dto.email,
                    hashed_password=cliente_dto.hashed_password,
                    telefone=cliente_dto.telefone,
                    ativo=cliente_dto.ativo) 

    def retornar_pelo_id(self, cliente_id: int) -> Cliente:
        retornoBd = self.repositorio.buscar_por_parametros(
            self.nomeTabela,
            None,
            [ParametroBd(campo = "id", valor = cliente_id)])

        if retornoBd == None: return None
        if len(retornoBd) < 1: return None

        retorno = retornoBd[0]
        return Cliente(
            id = retorno['id'], 
            cpf = retorno['cpf'], 
            nome = retorno['nome'], 
            email = retorno['email'], 
            hashed_password = retorno['hashed_password'], 
            telefone = retorno['telefone'], 
            ativo = retorno['ativo'])
    
    def retornar_pelo_cpf(self, cliente_cpf: str) -> Cliente:
        retornoBd = self.repositorio.buscar_por_parametros(
            self.nomeTabela,
            None,
            [ParametroBd(campo = "cpf", valor = cliente_cpf)])

        if retornoBd == None: return None
        if len(retornoBd) < 1: return None

        retorno = retornoBd[0]
        return Cliente(
            id = retorno['id'], 
            cpf = retorno['cpf'], 
            nome = retorno['nome'], 
            email = retorno['email'], 
            hashed_password = retorno['hashed_password'], 
            telefone = retorno['telefone'], 
            ativo = retorno['ativo'])
    
    def retornar_pelo_email(self, cliente_email: str) -> Cliente:
        retornoBd = self.repositorio.buscar_por_parametros(
            self.nomeTabela,
            None,
            [ParametroBd(campo = "email", valor = cliente_email)])

        if retornoBd == None: return None
        if len(retornoBd) < 1: return None

        retorno = retornoBd[0]
        return Cliente(
            id = retorno['id'], 
            cpf = retorno['cpf'], 
            nome = retorno['nome'], 
            email = retorno['email'], 
            hashed_password = retorno['hashed_password'], 
            telefone = retorno['telefone'], 
            ativo = retorno['ativo'])
        
    def editar(self, cliente_dto: ClienteDTO) -> bool:
        parametros: List[ParametroBd] = []
        parametros.append(ParametroBd(campo = "cpf", valor = cliente_dto.cpf))
        parametros.append(ParametroBd(campo = "nome", valor = cliente_dto.nome))
        parametros.append(ParametroBd(campo = "email", valor = cliente_dto.email))
        parametros.append(ParametroBd(campo = "hashed_password", valor = cliente_dto.hashed_password))
        parametros.append(ParametroBd(campo = "telefone", valor = cliente_dto.telefone))
        parametros.append(ParametroBd(campo = "ativo", valor = cliente_dto.ativo))
        
        retornoBd = self.repositorio.editar(
            self.nomeTabela,
            [ParametroBd(campo = "id", valor = cliente_dto.id)],
            parametros
        )
        if retornoBd == None: return None
        
        cliente_editado = self.repositorio.buscar_por_parametros(
            self.nomeTabela,
            None,
            [ParametroBd(campo = "id", valor = cliente_dto.id)])

        if cliente_editado == None: return None
        if len(cliente_editado) < 1: return None

        p = cliente_editado[0]
        return Cliente(
                    cpf=p['cpf'],
                    email=p['email'],
                    hashed_password=p['hashed_password'],
                    telefone=p['telefone'],
                    id = p['id'],
                    nome = p['nome'],
                    ativo = p['ativo']) 

    def deletar(self, cliente_id: int) -> bool:
        self.repositorio.deletar(
            self.nomeTabela,
            [ParametroBd(campo = "id", valor = cliente_id)]
        )
        return True
