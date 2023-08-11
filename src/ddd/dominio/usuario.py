from datetime import datetime

from pydantic import BaseModel, Field


class ParamUsuario(BaseModel):
    nome: str
    email: str
    cel: str


class Usuario(BaseModel):
    id: int = Field(alias='_id')
    nome: str
    email: str
    cel: str
    criado_em: datetime = Field(default_factory=datetime.now)
    alterado_em: datetime | None = None
