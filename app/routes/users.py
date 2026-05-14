from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from jose import JWTError, jwt

from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import hash_password
from app.core.config import JWT_SECRET_KEY, JWT_ALGORITHM

router = APIRouter(prefix="/users", tags=["users"])


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    user_data: UserCreate,
    db: Session = Depends(get_db)
):
    """
    Crear un nuevo usuario
    
    - **full_name**: Nombre completo del usuario
    - **username**: Nombre de usuario único
    - **password**: Contraseña (será hasheada con Argon2)
    
    Retorna la información del usuario creado
    """
    
    # Verificar si el usuario ya existe
    existing_user = db.query(User).filter(User.username == user_data.username).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"El nombre de usuario '{user_data.username}' ya está registrado"
        )
    
    # Hashear la contraseña con Argon2
    password_hash = hash_password(user_data.password)
    
    # Crear nuevo usuario
    new_user = User(
        full_name=user_data.full_name,
        username=user_data.username,
        password_hash=password_hash
    )
    
    # Guardar en la base de datos
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user

@router.get("/me")
async def get_current_user_info(
    request: Request,
    db: Session = Depends(get_db)
):
    """
    Obtener la información del usuario autenticado.

    El token puede venir desde:
    - Cookie: access_token
    - Header: Authorization: Bearer <token>
    """

    token = None

    authorization = request.headers.get("Authorization")

    if authorization and authorization.startswith("Bearer "):
        token = authorization.replace("Bearer ", "")

    cookie_token = request.cookies.get("access_token")

    if not token and cookie_token:
        if cookie_token.startswith("Bearer "):
            token = cookie_token.replace("Bearer ", "")
        else:
            token = cookie_token

    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No autorizado"
        )

    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token inválido"
            )

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido"
        )

    user = db.query(User).filter(User.username == username).first()

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario no encontrado"
        )

    return {
        "id": user.id,
        "full_name": user.full_name,
        "username": user.username,
        "password_hash": user.password_hash
    }