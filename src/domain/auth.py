from pydantic import BaseModel

class AuthCredentials(BaseModel):
    username: str
    password: str

class AuthResponse(BaseModel):
    access_token: str
