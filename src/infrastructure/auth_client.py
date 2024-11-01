import httpx
from src.domain.auth import AuthCredentials

class AuthClient:
    BASE_URL = "https://api.strateegia.digital/users/v1"

    async def login(self, credentials: AuthCredentials):
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Orimole/1.0"  # Opcional, mas pode ser necessário
        }
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.BASE_URL}/auth/signin",
                json={"username": credentials.username, "password": credentials.password},
                headers=headers
            )
            if response.status_code == 200:
                return response.json().get("access_token")
            else:
                raise Exception(f"Failed to authenticate with Strateegia: {response.text}")
