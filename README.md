# Parcial 2 - Autenticación Completa

Proyecto de autenticación completa con FastAPI, implementando endpoints de registro y login con OAuth2.

## Características

- Registro de usuarios con contraseñas hasheadas con Argon2
- Login con validación de credenciales
- Tokens JWT para autenticación
- Endpoint `/users/me` para obtener información del usuario autenticado
- Base de datos SQLite con SQLAlchemy

## Requisitos

- Python 3.9+
- Poetry

## Instalación

```bash
poetry install
```

## Ejecución

```bash
poetry run uvicorn app.main:app --reload
```

## Endpoints

- `POST /users` - Crear usuario
- `POST /login` - Autenticación de usuario
- `GET /users/me` - Obtener información del usuario autenticado
