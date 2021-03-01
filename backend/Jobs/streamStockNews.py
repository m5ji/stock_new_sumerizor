from kafka import KafkaProducer
from time import sleep
import json

with open('/usr/src/app/ML/files/newfilterMock.json') as f:
  data = json.load(f)

producer = KafkaProducer(bootstrap_servers='kafka:9092', api_version=(2,0,2))
for article in data['articles']:
    print(article)
    producer.send('stockNewsTitle', json.dumps(article).encode('utf-8'))
    sleep(5)

