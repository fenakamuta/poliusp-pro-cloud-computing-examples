# Yahoo Finance Pipeline Configuration

# Stock tickers to fetch data for
TICKERS = ['MSFT', 'AAPL', 'GOOG', 'NU']

# Google Cloud Project configuration
PROJECT_ID = "poli-usp-pro-cloud-computing"

# Google Cloud Storage configuration
BUCKET_NAME = "poliusp-pro-exemplo-aula"
BLOB_NAME = 'yahoo_finance/tickers.csv'

# BigQuery configuration
DATASET_ID = 'yahoo_finance'
TABLE_ID = 'tickers'

# Data fetching configuration
HISTORICAL_PERIOD = '36mo'  # 36 months of historical data 