from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.db.database import Base


class User(Base):
    """Modelo de usuario en la base de datos"""
    
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)  # Nombre completo
    username = Column(String(100), unique=True, index=True, nullable=False)  # Nombre de usuario único
    password_hash = Column(String(255), nullable=False)  # Contraseña hasheada con Argon2
    created_at = Column(DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, full_name={self.full_name})>"
