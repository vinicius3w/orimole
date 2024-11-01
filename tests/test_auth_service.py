import pytest
from src.domain.auth import AuthCredentials
from src.application.auth_service import AuthService
from src.infrastructure.auth_client import AuthClient

class MockAuthClient(AuthClient):
    async def login(self, credentials: AuthCredentials):
        if credentials.username == "valid_user" and credentials.password == "valid_password":
            return "mock_token"
        else:
            raise Exception("Authentication failed")

@pytest.fixture
def auth_service():
    return AuthService(auth_client=MockAuthClient())

@pytest.mark.asyncio
async def test_authenticate_success(auth_service):
    credentials = AuthCredentials(username="valid_user", password="valid_password")
    token = await auth_service.authenticate(credentials)
    assert token == "mock_token"

@pytest.mark.asyncio
async def test_authenticate_failure(auth_service):
    credentials = AuthCredentials(username="invalid_user", password="wrong_password")
    with pytest.raises(Exception, match="Authentication failed"):
        await auth_service.authenticate(credentials)
