# 📊 Desafio Técnico — Engenharia de Dados (Winnin)

Este repositório contém a solução completa do desafio técnico proposto para Engenheiro(a) de Dados Sênior.  
O projeto está dividido em duas partes:

- **Parte 1 — Implementação prática (Databricks Community Edition)**
- **Parte 2 — Arquitetura e Documentação**

---

## 🚀 Parte 1 — Implementação Prática no Databricks

### 🔧 Pré-requisitos
- Conta no [Databricks Community Edition](https://community.cloud.databricks.com/)
- Criar um **cluster** ativo no menu *Compute*
- Upload dos arquivos JSON (`wiki_pages.json.gz` e `posts_creator.json.gz`) em *Catalog → Create Table → Drop Files to Upload*

### 📒 Notebooks
1. `1 - create_table_creators_scrape_wiki`
   - Lê `wiki_pages.json.gz`
   - Cria a tabela `default.creators_scrape_wiki`

2. `2 - create_table_posts_creator`
   - Lê `posts_creator.json.gz`
   - Cria a tabela `default.posts_creator`

3. `3 - create_table_user_yt_from_wikipedia_api`
   - Consulta a **API da Wikipedia**
   - Cria a tabela `default.users_yt (user_id, wiki_page)`

4. `4 - analyze_creators`
   - Top 3 posts por **likes** nos últimos 6 meses
   - Top 3 posts por **views** nos últimos 6 meses
   - `yt_users` presentes em `posts_creator` mas ausentes em `users_yt`
   - Quantidade de publicações por mês
   - **Extra 1:** meses sem posts preenchidos com `0`
   - **Extra 2:** pivot com `user_id` e meses como colunas

🔧 Extra:

5. `5 - platinum_features`
   - Geração de features avançadas (`engajamento`, `CTR`, `score normalizado`)
   - Cria tabela `platinum.creators_features`

6. `6 - data_quality_checks`
   - Checagem de **schema** (colunas obrigatórias e tipos)
   - Checagem de **nulls, duplicados, ranges de datas**
   - Exibição de **alertas de inconsistência**

---

## 🏗️ Parte 2 — Arquitetura & Documentação

📂 Estrutura de documentação:

****************- `docs/arquitetura_pipeline.md`  
*****************  Explica o **fluxo de dados (Bronze → Silver → Gold → Platinum)** e inclui um **diagrama visual** com Prefect e monitoramento.

- `docs/data_contract_posts.json`  
  Contrato de schema para os posts.

- `docs/adrs/ADR-0001-orquestrador.md`  
  Justifica escolha do **Prefect** como orquestrador.

- `docs/adrs/ADR-0002-armazenamento.md`  
  Justifica uso de **Delta Lake + Databricks** como armazenamento.

📂 Infraestrutura:

- `infra/prefect_flows.py`  
  Exemplo de fluxo orquestrado no Prefect.

- `infra/terraform/README.md`  
  Placeholder para provisionamento futuro (infra como código).

📂 CI/CD:

- `.github/workflows/ci.yml`  
  Pipeline de **lint + testes automáticos**.

---

## ⚙️ Como Rodar

### 1. Executar notebooks no Databricks
- Faça upload dos notebooks (`1` a `6`) no **Workspace**
- Execute célula por célula na ordem acima

### 2. Rodar Prefect localmente
```bash
pip install prefect
python infra/prefect_flows.py
