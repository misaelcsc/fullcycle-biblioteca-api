# ADR 001 — Escolha de FastAPI + SQLAlchemy para a API da Biblioteca

## Status
Aceito

## Contexto
Precisávamos de um framework Python moderno para construir uma API REST de gerenciamento de biblioteca, com suporte a validação de dados, ORM e boa experiência de desenvolvimento.

## Decisão
Escolhemos **FastAPI** como framework web e **SQLAlchemy** como ORM, com **PostgreSQL** como banco de dados.

### Alternativas consideradas
- **Flask + Flask-SQLAlchemy**: mais maduro, mas exige mais boilerplate e validação manual.
- **Django REST Framework**: muito opinativo e pesado para o escopo do projeto.
- **Tortoise ORM / SQLModel**: promissores, mas com comunidade menor.

## Consequências
- Validação automática via Pydantic (schemas).
- Geração automática de OpenAPI/Swagger.
- Tipagem estática melhora manutenibilidade.
- Curva de aprendizado baixa para a equipe.