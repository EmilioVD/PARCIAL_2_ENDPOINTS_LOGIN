from passlib.context import CryptContext

# Configurar contexto de hashing con Argon2
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
DUMMY_PASSWORD_HASH = pwd_context.hash("dummy-password-for-timing")


def hash_password(password: str) -> str:
    """
    Hashear una contraseña con Argon2
    
    Args:
        password: Contraseña en texto plano
        
    Returns:
        Contraseña hasheada
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verificar una contraseña contra su hash Argon2
    
    Args:
        plain_password: Contraseña en texto plano
        hashed_password: Hash de la contraseña
        
    Returns:
        True si la contraseña coincide, False en caso contrario
    """
    return pwd_context.verify(plain_password, hashed_password)


def run_dummy_password_check(password: str) -> None:
    """Ejecuta una verificación dummy para mantener tiempos similares en login."""
    pwd_context.verify(password, DUMMY_PASSWORD_HASH)
