from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import API_TITLE, API_VERSION
from app.db.database import create_tables
from app.routes import auth, users

# Importar modelos para que SQLAlchemy los reconozca
from app.models.user import User


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Gestionar eventos del ciclo de vida de la aplicación
    """
    create_tables()
    yield
  


app = FastAPI(
    title=API_TITLE,
    version=API_VERSION,
    lifespan=lifespan,
    description="API de autenticación completa con FastAPI, SQLAlchemy y JWT"
)


@app.get("/")
async def root():
    return {
        "message": "API de autenticación completa con FastAPI",
        "docs": "/docs",
        "redoc": "/redoc"
    }



app.include_router(users.router)
app.include_router(auth.router)



