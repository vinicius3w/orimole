import asyncio
import httpx
from dotenv import load_dotenv
import os

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")

async def test_login():
    async with httpx.AsyncClient() as client:
        response = await client.post("http://127.0.0.1:8000/auth/login", json={
            "username": USERNAME,
            "password": PASSWORD
        })
        if response.status_code == 200:
            print("Login bem-sucedido!")
            print("Token:", response.json().get("access_token"))
        else:
            print("Falha no login:", response.status_code, response.text)

# Executa o teste de forma assíncrona
asyncio.run(test_login())
