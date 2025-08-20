# ADR-0001 — Orquestrador de Pipeline de Dados

## Contexto
Precisamos de um orquestrador para agendar, monitorar e executar os pipelines de ingestão e transformação de dados.

## Alternativas Consideradas
- **Airflow**: robusto, mas pesado para setup local.
- **Luigi**: simples, mas menos ativo na comunidade.
- **Prefect**: leve, moderno, fácil integração com Python e Databricks.

## Decisão
Optamos pelo **Prefect** como orquestrador principal.

## Consequências
- Pipelines descritos como código Python puro.
- Fácil integração com o GitHub Actions para CI/CD.
- Possibilidade de futura migração para Prefect Cloud se necessário.

