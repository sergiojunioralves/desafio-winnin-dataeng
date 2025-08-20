# ADR-0002 — Armazenamento de Dados

## Contexto
Precisamos escolher uma tecnologia de armazenamento para dados brutos, limpos e derivados.

## Alternativas Consideradas
- **PostgreSQL**: não ideal para grandes volumes de dados analíticos.
- **S3 + Parquet**: bom para arquivos, mas sem suporte nativo a time travel.
- **Delta Lake (Databricks)**: combina escalabilidade, versionamento e suporte a ACID.

## Decisão
Optamos por **Delta Lake no Databricks** como principal camada de armazenamento.

## Consequências
- Suporte a transações ACID.
- Time Travel para auditoria e reprocessamento.
- Integração nativa com Spark e Databricks SQL.

