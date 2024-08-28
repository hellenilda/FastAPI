from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional(int) = None # type: ignore
    titulo: str
    aulas: int
    horas: int