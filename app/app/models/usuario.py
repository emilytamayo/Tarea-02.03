from sqlalchemy import Column, Integer, String, Enum
from ..database import Base

class Rol(str, Enum):
    administrador = "administrador"
    profesor = "profesor"
    estudiante = "estudiante"
    padre = "padre"
    administrativo = "administrativo"

class Permiso(str, Enum):
    leer = "leer"
    escribir = "escribir"
    eliminar = "eliminar"

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    correo = Column(String, unique=True, index=True)
    rol = Column(Enum(Rol))
    permisos = Column(Enum(Permiso))
