from kafka import KafkaProducer
from time import sleep


producer = KafkaProducer(bootstrap_servers='kafka:9092', api_version=(2,0,2))
for e in range(1000):
    data = {'number' : e}
    producer.send('stockNewsTitle', b'Tesla Needs To Increase Production Now, Elon Musk Says In Leaked Email')
    sleep(5)

