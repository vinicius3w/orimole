from fastapi import FastAPI
from starlette.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from src.presentation.auth_controller import router as auth_router

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Criação da aplicação FastAPI
app = FastAPI(
    title="Orimole",
    description="API para coletar indicadores e métricas de jornadas estratégicas",
    version="1.0.0"
)

# Adiciona o middleware de segurança para hosts confiáveis
app.add_middleware(TrustedHostMiddleware, allowed_hosts=["127.0.0.1", "localhost"])

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost", "http://127.0.0.1"],  # Adicione aqui os domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos (GET, POST, etc.)
    allow_headers=["*"]   # Permite todos os cabeçalhos
)

# Incluir rotas do módulo de autenticação
app.include_router(auth_router, prefix="/auth", tags=["Autenticação"])

# Ponto de entrada para rodar a aplicação
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
