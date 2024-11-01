import base64
import httpx
from src.domain.auth import AuthCredentials

class AuthClient:
    BASE_URL = "https://api.strateegia.digital/users/v1"

    async def login(self, credentials: AuthCredentials):
        basic_auth = base64.b64encode(
            f"{credentials.username}:{credentials.password}".encode()
        ).decode()
        
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Basic {basic_auth}",
            "User-Agent": "Orimole/1.0"
        }
        
        payload = {
            "keepConnected": True
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.BASE_URL}/auth/signin",
                json=payload,
                headers=headers
            )
            
            if response.status_code == 200:
                return response.json().get("access_token")
            else:
                raise Exception(f"Failed to authenticate with Strateegia: {response.text}")
