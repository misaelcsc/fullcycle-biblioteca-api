# Desempenho — Smoke Test com k6

## Objetivo
Validar que o endpoint principal (`POST /loans/`) responde dentro de um SLO aceitável sob carga leve.

## SLO definido
- **p95 < 500ms** para `POST /loans/`

## Como rodar

1. Suba a API:
   ```bash
   docker-compose up --build -d