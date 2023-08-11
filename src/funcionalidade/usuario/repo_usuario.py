from typing import Type

from src.funcionalidade.usuario.modelo_usuario import Usuario
from src.funcionalidade.repositorios.repositorio_memoria import Repositorio


class RepoUsuario(Repositorio[Usuario]):
    def modelo(self) -> Type:
        return Usuario
