from kafka import KafkaConsumer, TopicPartition
import json

consumer = KafkaConsumer(
    'host-msg',
    bootstrap_servers='localhost:9092'
)
# consumer.assign([TopicPartition('host-msg', 0)])

for message in consumer:
    print(message.value.decode('utf-8'))