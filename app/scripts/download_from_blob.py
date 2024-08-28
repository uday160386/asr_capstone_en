from azure.storage.blob import BlobClient
import soundfile

connection_string = "<blob connection strin>"
def download_blog_file_content_to_wav(blobname, file_path):
    blob = BlobClient.from_connection_string(conn_str=connection_string, container_name="asrcontainer", blob_name=blobname)
    with open(file_path, "wb") as my_blob:
        stream = blob.download_blob()
        data = stream.readall()
        my_blob.write(data)
        
    restore_wav(file_path)

def restore_wav(file_path):
    data, samplerate = soundfile.read(file_path)
    soundfile.write(file_path, data, samplerate, subtype='PCM_16')