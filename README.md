# Tech Challenge Fase 1 - NPS Preditivo

Projeto de Ciencia de Dados para analisar fatores que influenciam o NPS de clientes de e-commerce e propor uma estrategia preditiva para antecipar risco de insatisfacao.

## Objetivo

Responder quais fatores operacionais impactam a satisfacao do cliente, identificar o que gera detratores e avaliar como modelos preditivos podem apoiar a empresa antes da aplicacao da pesquisa de NPS.

## Metodologia CRISP-DM

1. Business Understanding: entendimento do problema, importancia do NPS e areas impactadas.
2. Data Understanding: leitura da base, dicionario de dados, qualidade inicial e analise exploratoria.
3. Data Preparation: ajuste de tipos, separacao de variaveis, criacao da classificacao de NPS e preparacao para modelos.
4. Modeling: regressao para prever nota de NPS e classificacao para categorizar clientes.
5. Evaluation: comparacao de metricas, interpretacao de negocio e escolha dos melhores modelos.
6. Deployment: proposta de uso pratico pela empresa, ainda pendente de empacotamento operacional.

## Estrutura

```text
tech_challenge_01/
|-- data/
|   |-- raw/
|       |-- desafio_nps_fase_1.csv          # base original do desafio
|-- docs/
|   |-- imagens/
|       |-- Titulo.png                      # imagem usada no notebook principal
|
|-- models/
|   |-- modelo_lr.pkl                       # modelo treinado para prever nota de NPS
|   |-- modelo_rf.pkl                       # modelo treinado para classificar NPS
|
|-- notebooks/
|   |-- Tech_Challenge_Notebook.ipynb       # notebook principal: EDA, modelagem e conclusoes
|   |-- preprocessamento_lr.ipynb           # apoio ao pre-processamento da regressao linear
|   |-- preprocessamento_rf.ipynb           # apoio ao pre-processamento da classificacao Random Forest
|
|   |-- main_lr.ipynb                       # execucao da previsao de NPS numerico
|   |-- main_rf.ipynb                       # execucao da classificacao de NPS
|
|-- outputs/
|   |-- data_regressao.csv                  # base com coluna nps_previsto
|   |-- data_classificacao.csv              # base com coluna nps_classificacao_prevista
|
|-- references/
|   |-- tech_challenge_fase_1_nps_preditivo.pdf
|
|-- reports/
|   |-- Apresentacao_NPS_Machine_Learning.pptx
|   |-- Apresentacao_NPS_Machine_Learning.pdf
|   |-- Apresentacao_NPS_Machine_Learning.mp4
|
|-- src/
|   |-- preprocessamento_lr.py              # preparo dos dados para regressao linear
|   |-- preprocessamento_rf.py              # preparo dos dados para Random Forest
|   |-- main_lr.py                          # gera outputs/data_regressao.csv
|   |-- main_rf.py                          # gera outputs/data_classificacao.csv
|
|-- requirements.txt                        # dependencias Python
|-- README.md                               # documentacao principal do projeto
|-- .gitignore                              # regras de versionamento
```

## Como Reproduzir

1. Coloque o arquivo `desafio_nps_fase_1.csv` em `data/raw/desafio_nps_fase_1.csv`.
2. Instale as dependencias:

```bash
pip install -r requirements.txt
```

3. Abra o Jupyter:

```bash
jupyter notebook
```

4. Execute os notebooks nesta ordem:

```text
notebooks/Tech_Challenge_Notebook.ipynb
notebooks/main_lr.ipynb
notebooks/main_rf.ipynb
```

O notebook `Tech_Challenge_Notebook.ipynb` faz a analise completa e salva os modelos finais em `models/`.
Os notebooks `main_lr.ipynb` e `main_rf.ipynb` carregam esses modelos e salvam as previsoes em `outputs/`.

Tambem e possivel gerar as saidas pelos scripts Python, desde que os modelos ja existam em `models/`:

```bash
python src/main_lr.py
python src/main_rf.py
```

## Status

O projeto esta organizado para a entrega em CRISP-DM. A base fica em `data/raw/`, os modelos finais em `models/`, as saidas de predicao em `outputs/` e os materiais executivos em `reports/`.
