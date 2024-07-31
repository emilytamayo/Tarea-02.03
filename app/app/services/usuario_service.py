from sqlalchemy.orm import Session
from ..repositories.usuario_repository import get_usuario, create_usuario, update_usuario
from ..schemas.usuario import UsuarioCreate, UsuarioUpdate

def get_usuario_service(db: Session, usuario_id: int):
    return get_usuario(db, usuario_id)

def create_usuario_service(db: Session, usuario: UsuarioCreate):
    return create_usuario(db, usuario)

def update_usuario_service(db: Session, usuario_id: int, usuario: UsuarioUpdate):
    return update_usuario(db, usuario_id, usuario)

