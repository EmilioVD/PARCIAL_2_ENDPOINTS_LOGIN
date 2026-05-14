import os
from dotenv import load_dotenv

load_dotenv()

# JWT Configuration
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "your-secret-key-change-in-production")
JWT_EXPIRATION_HOURS = int(os.getenv("JWT_EXPIRATION_HOURS", "0.05"))  # 3 minutos

# Database Configuration
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")

# API Configuration
API_TITLE = "Parcial 2 - Autenticación Completa"
API_VERSION = "1.0.0"
