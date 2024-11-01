from fastapi import APIRouter, HTTPException, Depends
from src.application.auth_service import AuthService
from src.domain.auth import AuthCredentials, AuthResponse

router = APIRouter()

@router.post("/login", response_model=AuthResponse)
async def login(credentials: AuthCredentials, auth_service: AuthService = Depends()):
    try:
        token = await auth_service.authenticate(credentials)
        return AuthResponse(access_token=token)  # Certifique-se de que está retornando um objeto Pydantic
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
