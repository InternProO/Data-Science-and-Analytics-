from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('iot_data', bootstrap_servers='localhost:9092', value_deserializer=lambda x: json.loads(x.decode('utf-8')))

for message in consumer:
    data = message.value
    # Perform real-time analysis here
    print(f"Received data: {data}")
