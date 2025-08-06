# fastapi-atletas

API REST construída com FastAPI para gerenciamento de atletas, categorias e centros de treinamento.

## Tecnologias utilizadas

- Python 3.11
- FastAPI
- SQLAlchemy 2.0
- Pydantic v2
- PostgreSQL
- Alembic (migrações)
- Docker e Docker Compose
- Uvicorn (server ASGI)

## Funcionalidades

- CRUD de atletas
- CRUD de categorias
- CRUD de centros de treinamento
- Relacionamentos entre entidades
- Validações com Pydantic
- Integração com banco de dados PostgreSQL
- Versionamento de schema com Alembic
- Respostas personalizadas com status code
- Tratamento de erros e exceções

## Como executar localmente

### Pré-requisitos

- Python 3.11+
- Docker e Docker Compose
- Git

### 1. Clone o repositório

```bash
git clone https://github.com/theysla/fastapi-atletas.git
cd fastapi-atletas

