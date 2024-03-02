from common.interfaces.dbconnection import DbConnection
from common.tipos import ParametroBd
import mysql.connector
from mysql.connector import MySQLConnection
from typing import Protocol, List, Dict
import sys
from datetime import datetime

class Parametros(Protocol):
    restricao: str
    valores: List[any]


class MySQLConnection (DbConnection):
    
    def open_database(self):
        if 'pytest' in sys.modules:
            host = '127.0.0.1'
        else:
            host = 'tc_database'

        self._conexao = mysql.connector.connect(
                    user='root',
                    password='ROOTPASS',
                    host=host, # Deve ser o mesmo nome do serviço/container criado no docker-compose.yml, (ou verificar no docker network)
                    port=3306,
                    database='TechChallenge'
                )
        self._cursor = self._conexao.cursor(dictionary=True)
    
    def buscar_todas(self, nomeTabela: str, campos: List[str] | None = None) -> List:
    	
        camposBusca = self.ajustar_campos_string(campos)
        sql = f"SELECT {camposBusca} FROM {nomeTabela};"
        self.open_database()
        self._cursor.execute(sql)
        rows = self._cursor.fetchall()
        self._conexao.close()
        return rows

    def buscar_por_parametros(self,
        nomeTabela: str,
        campos: List[str] | None,
        parametros: List[ParametroBd]):
        
        camposBusca = self.ajustar_campos(campos)
        parametrosBusca = self.preparar_parametros_busca(parametros)
        sql = f"SELECT {camposBusca} FROM {nomeTabela} WHERE {" AND ".join(parametrosBusca)}"
        print(sql)
        self.open_database()
        self._cursor.execute(sql)
        
        rows = self._cursor.fetchall()
        self._conexao.close()
        return rows
    
    def inserir(self, nomeTabela: str, parametros: List[ParametroBd]):
        nomesCampos: List[any] = []
        nomesValores: List[str | int | float | bool] = []

        for item in parametros:
            nomesCampos.append(item.campo)
            if type(item.valor) == bool: valor = int(item.valor)
            else: valor = item.valor
            nomesValores.append(valor)
        print(nomesCampos)
        print(nomesValores)

        sql = f"""INSERT INTO {nomeTabela} 
            ({", ".join(nomesCampos)}) 
            VALUES ({self.ajustar_campos_string(nomesValores)});"""
        print(sql)
        self.open_database()
        self._cursor.execute(sql)
        self._conexao.commit()
        self._conexao.close()
        return True
    
    def editar(self, nomeTabela: str, condicoes: list[ParametroBd], parametros: list[ParametroBd]):
        parametrosBusca = self.preparar_parametros_busca(parametros)
        condicoesBusca = self.preparar_parametros_busca(condicoes)
        sql = f"""UPDATE {nomeTabela}
            SET {", ".join(parametrosBusca)}
            WHERE  {" AND ".join(condicoesBusca)}"""
        print(sql)
        self.open_database()
        self._cursor.execute(sql)
        self._conexao.commit()
        self._conexao.close()
        return True

    def deletar(self, nomeTabela, condicoes = list[ParametroBd]):
        
        condicoesBusca = self.preparar_parametros_busca(condicoes)

        sql = f"""DELETE FROM {nomeTabela} 
                WHERE {" AND ".join(condicoesBusca)}"""
        print(sql)
        self.open_database()
        self._cursor.execute(sql)
        self._conexao.commit()
        self._conexao.close()
        
    def preparar_parametros_busca(self, 
        params: List[ParametroBd] | None):
        
        if params == None:
            return ""

        camposRestricao: List[str] = []
        
        for item in params:
            # print(item.campo, " --> ", item.valor, " --> ", type(item.valor))
            if type(item.valor) == bool:
                camposRestricao.append(f"{item.campo} = {int(item.valor)}")
            elif type(item.valor) == datetime or type(item.valor) == str:
                camposRestricao.append(f"{item.campo} = '{(item.valor)}'")
            elif item.valor != None:
                camposRestricao.append(f"{item.campo} = {item.valor}")
        return camposRestricao
    
    # def preparar_parametros_string(self, 
    #     params: List[ParametroBd] | None):


    #     if params == None:
    #         return ""

    #     camposRestricao: List[str] = []
        
    #     for item in params:
    #         valor = item.valor
    #         if type(item.valor) == str:
    #             valor = "'" + item.valor + "'"
    #         if item.valor != None:
    #             camposRestricao.append(f"{item.campo} = {valor}")
    #     return camposRestricao

    def ajustar_campos(self, campos: List[str] | None) -> str:
        if campos == None:
            return " * "
        return ", ".join(campos)        

    def ajustar_campos_string(self, campos: List[any] | None) -> str:
        if campos == None:
            return " * "
        else:
            valores = []
            for campo in campos:
                if type(campo) == str:
                    valores.append("'" + campo + "'")
                elif type(campo) == bool:
                    valores.append("1")
                elif campo == None:
                    valores.append("''")
                else:
                    valores.append(str(campo))

        return ", ".join(valores)
            
