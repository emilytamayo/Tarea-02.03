from fastapi import FastAPI
from .database import engine, Base
from .controllers.usuario_controller import router as usuario_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(usuario_router, prefix="/api/v1", tags=["usuarios"])
