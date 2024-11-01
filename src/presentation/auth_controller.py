from fastapi import APIRouter, Depends, HTTPException

from src.application.auth_service import AuthService
from src.domain.auth import AuthCredentials, AuthResponse

router = APIRouter()


@router.post("/login", response_model=AuthResponse)
async def login(credentials: AuthCredentials, auth_service: AuthService = Depends(lambda: AuthService())):
    try:
        token = await auth_service.authenticate(credentials)
        # Certifique-se de que está retornando um objeto Pydantic
        return AuthResponse(access_token=token)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
