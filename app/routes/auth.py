from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.core.config import JWT_EXPIRATION_MINUTES
from app.core.jwt_utils import create_access_token
from app.core.security import run_dummy_password_check, verify_password
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import TokenResponse

router = APIRouter(tags=["auth"])


@router.post("/login", response_model=TokenResponse)
async def login(
    response: Response,
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """Autentica al usuario con formulario OAuth2 y emite JWT en body y cookie."""
    user = db.query(User).filter(User.username == form_data.username).first()

    if not user:
        run_dummy_password_check(form_data.password)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=JWT_EXPIRATION_MINUTES),
    )

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        max_age=JWT_EXPIRATION_MINUTES * 60,
        expires=JWT_EXPIRATION_MINUTES * 60,
        samesite="lax",
    )

    return TokenResponse(access_token=access_token)