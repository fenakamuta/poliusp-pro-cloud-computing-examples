import pandas as pd
import yfinance as yf
from google.cloud import storage
from google.cloud import bigquery
from config import TICKERS, PROJECT_ID, BUCKET_NAME, BLOB_NAME, DATASET_ID, TABLE_ID, HISTORICAL_PERIOD


def get_data(tickers):
    """
    Fetches 36 months of historical stock data for given ticker symbols.
    
    Args:
        tickers (list): List of stock ticker symbols
        
    Returns:
        pandas.DataFrame: Combined historical data for all tickers
    """
    df_tickers = pd.DataFrame()
    for ticker in tickers:
        df_ticker = yf.Ticker(ticker).history(period=HISTORICAL_PERIOD)
        df_ticker['Ticker'] = ticker
        df_tickers = pd.concat([df_tickers, df_ticker])
        
    return df_tickers


def write_df_to_gcs_blob(df, gcs_client, bucket_name, blob_name):
    """Writes a pandas DataFrame to a blob in Google Cloud Storage.

    Args:
        df: The pandas DataFrame to write.
        gcs_client: The Google Cloud Storage client.
        bucket_name: The name of the GCS bucket.
        blob_name: The name of the blob within the bucket.
    """
    bucket = gcs_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)

    # Convert DataFrame to CSV string
    csv_data = df.to_csv(index=True)

    # Upload the CSV data to the blob
    blob.upload_from_string(csv_data, content_type='text/csv')
    print(f"DataFrame successfully written to gs://{bucket_name}/{blob_name}")


def load_gcs_to_bigquery(bq_client, gcs_uri, project_id, dataset_id, table_id):
    """Loads data from Google Cloud Storage to BigQuery table.
    
    Args:
        bq_client: BigQuery client instance
        gcs_uri: GCS URI of the source file (gs://bucket/file)
        project_id: Google Cloud project ID
        dataset_id: BigQuery dataset ID
        table_id: BigQuery table ID
        
    Returns:
        BigQuery job result
    """
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,
        autodetect=True,
        write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE
    )

    table_ref = bq_client.dataset(dataset_id, project=project_id).table(table_id)

    load_job = bq_client.load_table_from_uri(
        gcs_uri,
        destination=table_ref,
        job_config=job_config
    )

    print(f"Loaded {load_job.output_rows} rows into {table_id}")
    return load_job.result()


def run_yahoo_finance_pipeline():
    # Project
    gcs_client = storage.Client(project=PROJECT_ID)
    bq_client = bigquery.Client(project=PROJECT_ID)

    # GCS
    gcs_uri = f'gs://{BUCKET_NAME}/{BLOB_NAME}'

    # Executing Pipeline
    df_tickers = get_data(TICKERS)
    write_df_to_gcs_blob(df_tickers, gcs_client, BUCKET_NAME, BLOB_NAME)
    load_gcs_to_bigquery(bq_client, gcs_uri, PROJECT_ID, DATASET_ID, TABLE_ID)


if __name__ == "__main__":
    run_yahoo_finance_pipeline()