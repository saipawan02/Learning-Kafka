from kafka import KafkaConsumer

def consumer():
    """Creates a KafkaConsumer instance which is used to read data from a Kafka topic.

    Arguments:
        topic_name (str): The name of the Kafka topic to read from.
        bootstrap_servers (str): A comma-separated list of host and port pairs that the consumer
            will use to bootstrap itself. Defaults to 'localhost:9092'.
    """
    consumer = KafkaConsumer(
        'host-msg',
        bootstrap_servers='localhost:9092'
    )

    for message in consumer:
        print(f'Received message: {message.value.decode("utf-8")}')


if __name__ == '__main__':
    consumer()