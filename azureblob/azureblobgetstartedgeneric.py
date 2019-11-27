#%%
# create the BlobClient
from azure.storage.blob import BlobClient
connection_string = "<connection-string>"
my_blob = BlobClient.from_connection_string(conn_str=connection_string, container_name="<container-name>", blob_name="<blob/file-name>")

#%%
# Upload a local file SampleSource.txt to the container <container-name> named <blob/file-name> 
with open("./SampleSource.txt", "rb") as data:
    my_blob.upload_blob(data)

#%%
# Download a file/blob named <blob/file-name> from the container <container-name> using BlobClient
with open("./BlobCopy.txt", "wb") as my_blob_dl:
    blob_data = my_blob.download_blob()
    blob_data.readinto(my_blob_dl)


# %%
# Enumarating all blobs within container
from azure.storage.blob import ContainerClient

container = ContainerClient.from_connection_string(conn_str="<connection-string>", container_name="<container-name>")

blob_list = container.list_blobs()
for blob in blob_list:
    print(blob.name + '\n')
