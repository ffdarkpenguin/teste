from typing import Type

from src.zorra_total.modelo_usuario import Usuario
from src.zorra_total.repositorio_memoria import Repositorio


class RepoUsuario(Repositorio[Usuario]):
    def modelo(self) -> Type:
        return Usuario
