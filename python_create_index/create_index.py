from elasticsearch import Elasticsearch
import time

file_json = open("json")
json_data = file_json.read()

es = Elasticsearch([{'host': 'localhost', 'ports': 9200}])

while es.ping() == False:
    time.sleep(10)

if es.ping() == True:
    es.index(index='index', doc_type='project', id=1, body=json_data)
    print("created index")
else:
    print("not created")
