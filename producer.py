import json
import time
import socket
import datetime
from kafka import KafkaProducer

hostname = socket.gethostname()

def produce():
    """
    Continuously produces data to Kafka with a timestamp and host information.

    The data is produced to the 'host-msg' topic on the Kafka broker running
    on 'localhost:9092'. The data is a JSON object with two keys: 'datetime'
    and 'host'. The 'datetime' key contains a string with the current time
    in ISO format, and the 'host' key contains the hostname of the machine
    running this code.

    The function runs continuously, producing data every second.
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

