# poliusp-pro-cloud-computing-examples

## 📚 Sobre este repositório

Este repositório contém exemplos práticos e códigos desenvolvidos durante as aulas de **Cloud Computing** da **PoliUSP Pro**. Aqui você encontrará implementações, demonstrações e exercícios relacionados aos conceitos de computação em nuvem.

## 🎯 Objetivo

O objetivo deste repositório é servir como material de referência e estudo, organizando os exemplos práticos vistos em sala de aula para facilitar o aprendizado e revisão dos conceitos de Cloud Computing.

## 📁 Estrutura do repositório

```
poliusp-pro-cloud-computing-examples/
├── README.md
├── requirements.txt
└── src/
    └── yahoo_finance/
        ├── main.py
        └── config.py
```

## 🚀 Projetos

### 📈 Yahoo Finance Data Pipeline

Um pipeline completo para coleta, armazenamento e análise de dados financeiros usando Google Cloud Platform.

#### ✨ Funcionalidades

- **Coleta de dados**: Busca dados históricos de ações via Yahoo Finance API
- **Armazenamento em nuvem**: Salva dados no Google Cloud Storage (GCS)
- **Data Warehouse**: Carrega dados no BigQuery para análise
- **Configuração flexível**: Arquivo de configuração separado para fácil customização

#### 🛠️ Tecnologias utilizadas

- **Python**: Linguagem principal
- **pandas**: Manipulação e análise de dados
- **yfinance**: API para dados financeiros
- **Google Cloud Storage**: Armazenamento de dados
- **Google BigQuery**: Data warehouse

#### 📋 Pré-requisitos

1. **Conta Google Cloud Platform** com projeto ativo
2. **Credenciais de autenticação** configuradas
3. **Python 3.7+** instalado
4. **Pacotes Python** listados em `requirements.txt`

#### ⚙️ Configuração

1. **Clone o repositório**:
   ```bash
   git clone <repository-url>
   cd poliusp-pro-cloud-computing-examples
   ```

2. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure as credenciais do Google Cloud**:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"
   ```

4. **Personalize a configuração** (opcional):
   - Edite `src/yahoo_finance/config.py` para modificar:
     - Tickers de ações
     - IDs do projeto GCP
     - Nomes de buckets e tabelas
     - Período de dados históricos

#### 🚀 Como executar

```bash
cd src/yahoo_finance
python main.py
```

#### 📊 Dados coletados

O pipeline coleta os seguintes dados para cada ticker configurado:
- **Preço de abertura** (Open)
- **Preço de fechamento** (Close)
- **Preço máximo** (High)
- **Preço mínimo** (Low)
- **Volume negociado** (Volume)
- **Data** (Date)
- **Símbolo da ação** (Ticker)

#### 🔧 Configuração personalizada

Edite o arquivo `config.py` para personalizar:

```python
# Tickers de ações
TICKERS = ['MSFT', 'AAPL', 'GOOG', 'NU']

# Configurações do Google Cloud
PROJECT_ID = "seu-projeto-id"
BUCKET_NAME = "seu-bucket-name"
DATASET_ID = 'yahoo_finance'
TABLE_ID = 'tickers'

# Período de dados históricos
HISTORICAL_PERIOD = '36mo'  # 36 meses
```

#### 📈 Fluxo do pipeline

1. **Extração**: Busca dados históricos via Yahoo Finance API
2. **Transformação**: Organiza dados em DataFrame pandas
3. **Carregamento**: 
   - Salva CSV no Google Cloud Storage
   - Carrega dados no BigQuery para análise

#### 🔍 Monitoramento

O pipeline exibe logs informativos durante a execução:
- Confirmação de upload para GCS
- Número de linhas carregadas no BigQuery
- Status de conclusão das operações

---

## 🚀 Como usar outros exemplos

1. Navegue pelas pastas para encontrar o tópico de interesse
2. Cada exemplo contém documentação explicativa
3. Sinta-se à vontade para experimentar e modificar os códigos

## 📖 Conteúdo

- **Yahoo Finance Data Pipeline**: Pipeline completo de dados financeiros
- Exemplos práticos de Cloud Computing
- Códigos demonstrados em aula
- Exercícios e soluções
- Material de referência

---

*Desenvolvido durante o curso de Cloud Computing da PoliUSP Pro*