from src.infrastructure.auth_client import AuthClient
from src.domain.auth import AuthCredentials

class AuthService:
    def __init__(self, auth_client: AuthClient):
        self.auth_client = auth_client

    async def authenticate(self, credentials: AuthCredentials):
        return await self.auth_client.login(credentials)
