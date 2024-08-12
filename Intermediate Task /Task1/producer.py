from kafka import KafkaProducer
import json
import time
import random

producer = KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=lambda v: json.dumps(v).encode('utf-8'))

while True:
    data = {'temperature': random.uniform(20.0, 25.0), 'humidity': random.uniform(30.0, 50.0)}
    producer.send('iot_data', data)
    time.sleep(1)
