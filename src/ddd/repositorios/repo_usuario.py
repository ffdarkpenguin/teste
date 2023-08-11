from typing import Type

from src.ddd.dominio.usuario import Usuario
from src.ddd.repositorios.repositorio_memoria import Repositorio


class RepoUsuario(Repositorio[Usuario]):
    def modelo(self) -> Type:
        return Usuario
