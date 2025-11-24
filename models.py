from pydantic import BaseModel, AnyUrl, Field
from typing import Optional

class CharacterBase(BaseModel):
    nombre: str = Field(..., min_length=1)
    descripcion: Optional[str] = None
    frase: Optional[str] = None
    video: Optional[AnyUrl] = None

class CharacterCreate(CharacterBase):
    pass

class CharacterUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    frase: Optional[str] = None
    video: Optional[AnyUrl] = None

class Character(CharacterBase):
    id: int
