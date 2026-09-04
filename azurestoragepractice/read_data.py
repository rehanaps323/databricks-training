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

# --- 3. Inspect what we got ---
print(df_flat.shape)
print(df_flat.columns.tolist())
print(df_flat.head())
print(f"Total records loaded: {len(df)}")