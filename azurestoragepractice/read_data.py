from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import pandas as pd
import io

account_url = "https://uae.blob.core.windows.net"
container_name = "rehanadataset"
blob_name = "ctg-studies.json"


credential = DefaultAzureCredential()
blob_service_client = BlobServiceClient(account_url, credential=credential)
container_client = blob_service_client.get_container_client(container_name)

blob_client = container_client.get_blob_client(blob_name)
stream = blob_client.download_blob().readall()
df = pd.read_json(io.BytesIO(stream))

# --- 2. Flatten the nested JSON column ---
df_flat = pd.json_normalize(df['protocolSection'])

# Create a Spark DataFrame from the flattened DataFrame
spark_df = spark.createDataFrame(df_flat)

# Save as Delta table
spark_df.write \
    .format("delta") \
    .mode("overwrite") \
    .saveAsTable("clinical_trials")

# Display it
display(spark_df)

