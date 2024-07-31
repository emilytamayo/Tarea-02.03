from pydantic import BaseModel
from typing import List, Optional

class UsuarioBase(BaseModel):
    nombre: str
    correo: str
    rol: str

class UsuarioCreate(UsuarioBase):
    contrasena: str

class UsuarioUpdate(UsuarioBase):
    permisos: List[str] = []
