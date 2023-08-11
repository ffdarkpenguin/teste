class Erro(Exception):
    def __init__(self, msg: str) -> None:
        self.msg = msg
        super().__init__(msg)


class NaoEncontrado(Erro):
    ...


class Duplicado(Erro):
    ...
