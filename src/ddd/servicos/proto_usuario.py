from typing import Protocol

from src.ddd.dominio.usuario import Usuario


class Repo(Protocol):
    def insere(self, param: Usuario):
        ...

    def busca_por_id(self, _id) -> Usuario:
        ...
