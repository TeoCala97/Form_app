from google.cloud import pubsub_v1
from google.cloud import bigquery
from google.cloud import storage
from google.oauth2 import service_account
import time 
import json


class GCP_gestor:
    def connect_client(project,buckets):
        global bucket
        client_storage= storage.Client(project=project)
        bucket = client_storage.get_bucket(buckets,)

    def publisher():
        publisher = pubsub_v1.PublisherClient()
        project_id = "sod-co-bi-sandbox"
        topic_id = "auto_campanhas"
        topic_path = publisher.topic_path(project_id, topic_id)
        message='{"name": "{topic_path}" }'
        data = message
        data = data.encode('utf-8')
        future = publisher.publish(topic_path, data)
        print(future.result())
        print(f"Published messages to {topic_path}.")
        return topic_path
    
    @staticmethod
    def post_form(json_name, formu):
        with open(json_name,'w') as j:
            json.dump(formu,j)      
        blob = bucket.blob(json_name)
        blob.upload_from_filename(json_name)
        
    
    def get_form():
        blob_get = bucket.get_blob('post_data.json')
        File= blob_get.download_as_string() 
        File = json.loads(File)
        if File['key_lecture'] == 0:
            while(File['key_lecture'] == 0):
                time.sleep(2)
                blob_get = bucket.get_blob('post_data.json')
                File = blob_get.download_as_string() 
                File = json.loads(File)
        return File
