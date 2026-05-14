# Guía de Uso - Entorno Virtual con FastAPI y Poetry

## ✅ Configuración Completada

El entorno virtual ha sido configurado exitosamente con FastAPI y Poetry. A continuación, encontrarás toda la información necesaria para trabajar con el proyecto.

## 📦 Estructura del Proyecto

```
PARCIAL_2_ENDPOINTS_LOGIN/
├── app/
│   ├── core/
│   │   └── config.py          # Configuración de la aplicación
│   ├── db/                     # Base de datos
│   ├── models/                 # Modelos de base de datos
│   ├── routes/                 # Endpoints de la API
│   ├── schemas/                # Esquemas Pydantic
│   ├── main.py                 # Aplicación principal
│   └── __init__.py
├── .env                        # Variables de entorno (local)
├── .env.example                # Ejemplo de variables de entorno
├── .gitignore                  # Archivos a ignorar en git
├── pyproject.toml              # Configuración de Poetry
├── poetry.lock                 # Versiones exactas instaladas
└── README.md                   # Documentación
```

## 🚀 Comandos Útiles

### Instalar Dependencias
```bash
poetry install
```

### Ejecutar la Aplicación
```bash
poetry run uvicorn app.main:app --reload
```
La API estará disponible en: `http://localhost:8000`

### Documentación Interactiva
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Ejecutar Tests
```bash
poetry run pytest
```

### Ejecutar Tests con Cobertura
```bash
poetry run pytest --cov=app
```

### Formatear Código
```bash
poetry run black app/
```

### Verificar Código (Linting)
```bash
poetry run flake8 app/
```

### Type Checking
```bash
poetry run mypy app/
```

## 🔑 Dependencias Instaladas

### Principales
- **FastAPI** (0.104.1) - Framework web
- **Uvicorn** (0.24.0) - Servidor ASGI
- **Pydantic** (2.4.2) - Validación de datos
- **SQLAlchemy** (2.0.23) - ORM para base de datos
- **PyJWT** (2.8.1) - Tokens JWT
- **Passlib** (1.7.4) - Hashing de contraseñas
- **Python-dotenv** (1.0.0) - Variables de entorno
- **Cryptography** (41.0.7) - Seguridad

### Desarrollo
- **Pytest** (7.4.3) - Testing
- **Black** (23.11.0) - Formateador de código
- **Flake8** (6.1.0) - Linter
- **MyPy** (1.7.0) - Type checking

## 🔐 Variables de Entorno

El archivo `.env` contiene:
- `JWT_ALGORITHM`: Algoritmo para generar JWT (HS256)
- `JWT_SECRET_KEY`: Clave secreta para JWT (CAMBIAR EN PRODUCCIÓN)
- `JWT_EXPIRATION_HOURS`: Duración del token (0.05 = 3 minutos)
- `DATABASE_URL`: URL de la base de datos SQLite

## 📝 Próximos Pasos

1. **Crear modelos de base de datos** en `app/models/`
2. **Crear esquemas Pydantic** en `app/schemas/`
3. **Implementar rutas/endpoints** en `app/routes/`
4. **Configurar la base de datos** en `app/db/`

## 🛠️ Entorno Virtual

Para activar el entorno virtual de Poetry:
```bash
poetry shell
```

Para salir:
```bash
exit
```

## 📚 Referencias Útiles

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Poetry Documentation](https://python-poetry.org/docs/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/)
- [JWT Documentation](https://pyjwt.readthedocs.io/)
