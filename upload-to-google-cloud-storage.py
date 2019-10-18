# Based on python snippet from https://cloud.google.com/storage/docs/uploading-objects

from google.cloud import storage
import os.path
from os import path
import time

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print('File {} uploaded to {}.'.format(
        source_file_name,
        destination_blob_name))

def check_file_exists():
    if path.exists("/root/client.ovpn"):
        upload_blob("/root/client.ovpn","<GCloud-Bucket>","client.ovpn")
    else:
        time.sleep(5)
        check_file_exists()

check_file_exists()
