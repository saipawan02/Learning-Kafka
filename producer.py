from kafka import KafkaProducer
import datetime
import time
import socket
import json

hostname = socket.gethostname()

def produce():
    """
    A function that continuously produces data to Kafka with a timestamp and host information.
    """

    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    while True:
        current_time = str(datetime.datetime.now())
        data = {
            'datetime': current_time, 
            'host': hostname
            }
        producer.send(
            topic='host-msg', 
            value=json.dumps(data).encode('utf-8')
        )
        print("Data sent: ", data)
        time.sleep(1)

if __name__ == '__main__':
    produce()

