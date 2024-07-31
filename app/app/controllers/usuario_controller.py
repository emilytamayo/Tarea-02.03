from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..schemas.usuario import UsuarioBase, UsuarioCreate, UsuarioUpdate
from ..services.usuario_service import get_usuario_service, create_usuario_service, update_usuario_service
from ..database import get_db

router = APIRouter()

@router.post("/usuarios/", response_model=UsuarioBase, tags=["usuarios"])
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    return create_usuario_service(db, usuario)

@router.get("/usuarios/", response_model=List[UsuarioBase], tags=["usuarios"])
def read_usuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    usuarios = get_usuarios_service(db, skip=skip, limit=limit)
    return usuarios

@router.get("/usuarios/{usuario_id}", response_model=UsuarioBase, tags=["usuarios"])
def read_usuario(usuario_id: int, db: Session = Depends(get_db)):
    db_usuario = get_usuario_service(db, usuario_id)
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return db_usuario

@router.put("/usuarios/{usuario_id}", response_model=UsuarioBase, tags=["usuarios"])
def update_usuario(usuario_id: int, usuario: UsuarioUpdate, db: Session = Depends(get_db)):
    return update_usuario_service(db, usuario_id, usuario)
