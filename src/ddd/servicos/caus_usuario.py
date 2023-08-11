from src.ddd.dominio.usuario import ParamUsuario, Usuario
from src.ddd.repositorios.repo_usuario import RepoUsuario
from src.ddd.servicos.proto_usuario import Repo


class GerenciadorUsuario:
    def __init__(self, repo: Repo) -> None:
        self.repo = repo

    def insere_usuario(self, param: ParamUsuario) -> Usuario:
        usuario = Usuario(_id=1, **param.model_dump())
        self.repo.insere(usuario)
        return usuario

    def get_por_id(self, _id: int) -> Usuario:
        return self.repo.busca_por_id(_id=_id)


repo_usuario = RepoUsuario()

gerente = GerenciadorUsuario(repo=repo_usuario)

param = ParamUsuario(nome='ff', email='ff@ff', cel='91234')

gerente.insere_usuario(param=param)

print(gerente.get_por_id(1))
