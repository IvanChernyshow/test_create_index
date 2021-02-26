from elasticsearch import Elasticsearch
import time, os, json

file_json = open("json")
json_data = json.loads(file_json.read())


host = os.environ.get('HOST')
port = os.environ.get('PORT')


es = Elasticsearch([{'host': host, 'port': port}])


def create_index():
    while es.ping() == False:
        time.sleep(10)
        print("conection refused")
        continue
    else:
        print("conection succesful")
        es.index(index=json_data['index'], doc_type=json_data['doc_type'], id=json_data['id'], body=json_data['body'])
        print("created index")

create_index()
