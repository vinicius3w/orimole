# Orimole

Orimole é um projeto de dashboard de código aberto desenvolvido em Python com FastAPI, projetado para coletar e apresentar indicadores, métricas, KPIs e OKRs de forma integrada a plataformas de design colaborativo, como a Strateegia.digital. Inspirado na cultura rica dos orixás e nos conceitos de iluminação e sabedoria, **Orimole** busca ser uma luz orientadora nas jornadas estratégicas.

## Índice
- [Sobre o Projeto](#sobre-o-projeto)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Instalação](#instalação)
- [Uso](#uso)
- [Contribuição](#contribuição)
- [Licença](#licença)
- [Contato](#contato)

## Sobre o Projeto
**Orimole** foi criado para facilitar a análise de dados estratégicos e proporcionar uma visualização clara de indicadores de performance em projetos colaborativos. Utilizando práticas de desenvolvimento modernas como Clean Architecture e princípios SOLID, o projeto busca ser robusto, escalável e fácil de manter.

## Estrutura do Projeto
O projeto segue uma estrutura modular para melhor organização e manutenção:

```
project-root/
│
├── src/
│   ├── presentation/          # Interface do usuário (controladores, rotas)
│   ├── application/           # Casos de uso e lógica de aplicação
│   ├── domain/                # Entidades e regras de negócio
│   └── infrastructure/        # Integração com serviços externos, como a API da Strateegia.digital
│
├── main.py                    # Ponto de entrada da aplicação
└── requirements.txt           # Dependências do projeto
```

## Tecnologias Utilizadas
- **Python 3.9+**
- **FastAPI**: Framework para criação de APIs rápidas e seguras.
- **httpx**: Cliente HTTP assíncrono.
- **Uvicorn**: Servidor ASGI para rodar a aplicação.
- **Pydantic**: Validação de dados.

## Instalação
### Pré-requisitos
Certifique-se de ter o Python 3.9+ instalado em sua máquina e um ambiente virtual configurado.

### Passos
1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/orimole.git
   cd orimole
   ```

2. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv env
   source env/bin/activate   # Linux/macOS
   env\Scripts\activate      # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicie a aplicação:
   ```bash
   uvicorn main:app --reload
   ```

## Uso
Após iniciar a aplicação, a API estará disponível em `http://127.0.0.1:8000`. Você pode acessar a documentação automática da API em `http://127.0.0.1:8000/docs`.

## Contribuição
Contribuições são bem-vindas! Siga as diretrizes de contribuição descritas no arquivo `CONTRIBUTING.md` (a ser criado).

## Licença
Este projeto é licenciado sob a [Apache-2.0 license](LICENSE).

## Contato
Desenvolvido por **Vinicius**. Para mais informações, entre em contato em [seu-email@example.com].
