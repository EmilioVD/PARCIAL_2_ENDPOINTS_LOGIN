from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from app.core.security import hash_password

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
