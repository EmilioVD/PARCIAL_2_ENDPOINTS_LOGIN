from fastapi import FastAPI
from app.core.config import API_TITLE, API_VERSION

app = FastAPI(title=API_TITLE, version=API_VERSION)


@app.get("/")
async def root():
    return {"message": "API de autenticación completa con FastAPI"}


# Importar routers aquí cuando estén listos
# from app.routes import users, auth
