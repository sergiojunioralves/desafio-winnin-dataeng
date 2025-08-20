# Arquitetura do Pipeline de Dados — Creators & Posts

## Visão Geral
O pipeline foi projetado para coletar, processar e analisar dados de criadores de conteúdo e seus posts em uma arquitetura moderna de dados, baseada em camadas (Bronze, Silver, Gold e Platinum).

## Camadas de Dados
- **Bronze**: dados brutos carregados diretamente de APIs, web scraping ou arquivos de origem (JSON, CSV). Exemplo: `wiki_pages.json.gz`, `posts_creator.json.gz`.
- **Silver**: dados limpos, padronizados e normalizados. Exemplo: tabelas `creators_scrape_wiki`, `posts_creator`.
- **Gold**: dados modelados e prontos para consumo analítico. Exemplo: `users_yt`, análises agregadas de posts.
- **Platinum**: features avançadas para Data Science / Machine Learning. Exemplo: `platinum_features`.

## Fluxo ETL/ELT
1. **Ingestão**: dados coletados via APIs da Wikipedia/YouTube ou arquivos de dump.
2. **Transformação**: limpeza de schema, tratamento de nulls, deduplicação, joins.
3. **Carga**: tabelas Delta Lake organizadas por camada no Databricks.

## Diagrama do Pipeline

```mermaid
flowchart TD
    A[Wikipedia API] -->|user_id| B[Bronze]
    A2[JSON Files] --> B[Bronze]
    B --> C[Silver - Tabelas Limpa]
    C --> D[Gold - Análises]
    D --> E[Platinum - Features Avançadas]
    D --> F[Data Quality Checks]

