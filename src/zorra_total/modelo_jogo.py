from pydantic import BaseModel, Field


class Jogo(BaseModel):
    id: int = Field(alias='_id')
    nome: str
