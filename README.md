# NYC Taxi Lakeflow Pipeline
**Teste Engenheiro de Dados – 3 Camadas com Lakeflow (ex-DLT), Expectations, camelCase e SQL Analytics**

---

## Visão Geral

Este projeto implementa um **pipeline completo de dados em 3 camadas (Bronze → Silver → Gold)** usando **Databricks Lakeflow (antigo Delta Live Tables / DLT)** para processar dados de **táxis amarelos de Nova York (NYC TLC)**.

**Objetivo**:  
Ingerir dados brutos, aplicar **qualidade com expectations**, **enriquecer com zonas**, e gerar **tabelas analíticas (Gold)** prontas para **responder perguntas de negócio via SQL**.

---

## Problemas de Negócio Respondidos

| # | Pergunta | Tabela Gold |
|---|--------|------------|
| 1 | Quais **horas do dia** têm **maior receita** e **maior ticket médio**? | `gold.default.goldRevenueByHour` |
| 2 | Qual o **% médio de gorjeta por dia da semana**? | `gold.default.goldTipByDayOfWeek` |
| 3 | Quais **zonas (pickup e dropoff)** geram **mais receita**? | `gold.default.goldTopZones` |

---

## Arquitetura Medalhão (3 Camadas)

| Camada | Tabela | Fonte | Saída | Qualidade |
|-------|--------|-------|-------|----------|
| **Bronze** | `bronze.default.yellow_taxi_tripdata_2025` | 9 arquivos Parquet (Jan–Set 2025) | Delta | camelCase + tipos |
| **Bronze** | `bronze.default.taxi_zone_lookup` | CSV | Delta | camelCase + tipos |
| **Silver** | `silver.default.silverTripsClean` | Bronze + join | Delta | Expectations + filtro |
| **Gold** | 3 tabelas analíticas | Silver | Delta | Agregações |

---

## Fonte de Dados

> **Página Oficial**: [https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)

### Arquivos Obrigatórios (2025)

| Tipo | Arquivo | Link |
|------|--------|------|
| **Yellow Taxi** | `yellow_tripdata_2025-01.parquet` | [Baixar](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) |
| | `yellow_tripdata_2025-02.parquet` | |
| | ... até `yellow_tripdata_2025-09.parquet` | |
| **Taxi Zone Lookup** | `taxi_zone_lookup.csv` | [Baixar CSV](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) |

> **Dica**: Use o **dicionário de dados (Data Dictionary)** na mesma página para entender os campos.

---

## Como Executar (Passo a Passo)

> **IMPORTANTE**:  
> - O repositório **já tem os 3 notebooks `.py` prontos** (`01_bronze_pipeline.py`, `02_silver_pipeline.py`, `03_gold_pipeline.py`)
> - **Falta apenas**:  
>   1. Executar o create_catalog.ipynb para gerar: `bronze`, `silver`, `gold`,`ingestao.default.ingestao_dados`
>   2. Fazer **upload dos dados**  
>   3. Rodar o pipeline

---

### 1. Clonar o Repositório (OBRIGATÓRIO)

```bash
git clone https://github.com/seu-usuario/nyc-taxi-lakeflow.git
