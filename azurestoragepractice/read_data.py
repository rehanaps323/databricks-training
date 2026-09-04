from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import pandas as pd
import io

# Azure Storage
account_url = "https://uae.blob.core.windows.net"
container_name = "rehanadataset"
blob_name = "ctg-studies.json"

# Get secret from Databricks
account_key = dbutils.secrets.get(scope="azure-storage", key="storage-key")

# Connect to Azure Blob Storage
blob_service_client = BlobServiceClient(account_url, credential=account_key)
container_client = blob_service_client.get_container_client(container_name)

blob_client = container_client.get_blob_client(blob_name)

# Download JSON
stream = blob_client.download_blob().readall()

# Read JSON
df = pd.read_json(io.BytesIO(stream))

#Flatten the nested JSON column 
df_flat = pd.json_normalize(df['protocolSection'])

# Create a Spark DataFrame from the flattened DataFrame
spark_df = spark.createDataFrame(df_flat)

# Save as Delta table
spark_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("clinical_trials")

# Display table
display(spark_df)

