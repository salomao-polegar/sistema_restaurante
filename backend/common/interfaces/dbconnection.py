from common.tipos import ParametroBd
from typing import Protocol

class DbConnection (Protocol):
  def buscar_por_parametros(nomeTabela: str, campos: list[str] | None, parametros: list[ParametroBd]):
    pass

  def buscar_todas(nomeTabela: str, campos: list[str] | None = None):
    pass

  def inserir(nomeTabela: str, parametros: list[ParametroBd]):
    pass

  def editar(nomeTabela: str, condicoes: list[ParametroBd], parametros: list[ParametroBd]):
    pass

  def deletar(nomeTabela, condicoes = list[ParametroBd]):
    pass