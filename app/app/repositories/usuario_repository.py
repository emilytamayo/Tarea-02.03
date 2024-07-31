from sqlalchemy.orm import Session
from ..models.usuario import Usuario
from ..schemas.usuario import UsuarioCreate, UsuarioUpdate

def get_usuario(db: Session, usuario_id: int):
    return db.query(Usuario).filter(Usuario.id == usuario_id).first()

def create_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def update_usuario(db: Session, usuario_id: int, usuario: UsuarioUpdate):
    db_usuario = get_usuario(db, usuario_id)
    if db_usuario:
        for key, value in usuario.dict().items():
            setattr(db_usuario, key, value)
        db.commit()
        db.refresh(db_usuario)
    return db_usuario

