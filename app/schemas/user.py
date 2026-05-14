from pydantic import BaseModel, Field
from datetime import datetime


class UserCreate(BaseModel):
    """Schema para crear un usuario nuevo creado en la base de datos"""
    full_name: str = Field(..., min_length=1, max_length=255, description="Nombre completo del usuario")
    username: str = Field(..., min_length=3, max_length=100, description="Nombre de usuario único")
    password: str = Field(..., min_length=6, description="Contraseña (mínimo 6 caracteres)")
    
    class Config:
        json_schema_extra = {
            "example": {
                "full_name": "Raúl Duarte",
                "username": "ProfeDuarte97",
                "password": "holitas de mar"
            }
        }


class UserResponse(BaseModel):
    """Schema para respuesta de usuario en la base de datos"""
    id: int
    full_name: str
    username: str
    created_at: datetime
    
    class Config:
        from_attributes = True
        json_schema_extra = {
            "example": {
                "id": 1,
                "full_name": "Raúl Duarte",
                "username": "ProfeDuarte97",
                "created_at": "2024-05-14T10:30:00"
            }
        }


class UserLogin(BaseModel):
    """Schema para login de usuario"""
    username: str = Field(..., description="Nombre de usuario")
    password: str = Field(..., description="Contraseña")
    
    class Config:
        json_schema_extra = {
            "example": {
                "username": "ProfeDuarte97",
                "password": "holitas de mar"
            }
        }


class UserInfo(BaseModel):
    """Schema para información del usuario autenticado"""
    id: int
    full_name: str
    username: str
    created_at: datetime
    
    class Config:
        from_attributes = True


class TokenResponse(BaseModel):
    """Schema para respuesta de autenticación."""
    access_token: str
    token_type: str = "bearer"
