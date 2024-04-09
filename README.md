
Kafka Server/kafka Broker:
===============

- usually hosted on 9092
- Kafka brokers can have multiple listeners. A listener is a combination of
    - Host/IP
    - Port
    - Protocol

Producer:
---------

- Connect to the broker to exchange information
- producer is responsible to write information in the topics
- This is done usually with a tcp connection with is bi-directional.


Producer published the data to the kafka broker.
This data is stored in topics. These data are identified using topic name and position (index).

Consumer:
---------

- Connects to the broker to accept the information.
- Consumer accepts the data from the topics
- This connection is also established using tcp protocol.

Topics:
-------

- These are the logical partitions of data where producer writes

Partition:
---------

- These are the partitions on the topic to distribute data for faster access.


Queue:
------

- A message is published once and consumed only once

Pub Sub:
--------

- Message is published once, Consumed many times.

Consumer Group:
----------------

- 1 consumer can consume from 1 or 1+ partitions
- 1 Partition can only be consumed by 1 consumer.
- 1 partitions can be consumed by multiple consumer in different groups.
- This will ensure parallel processing as different consumer will consume data from multiple partitions at the same time.


Spinning the zookeeper instance:
--------------------------------

- `docker run --name zookeeper -p 2181:2181 zookeeper`

Spinning the Kafka container:
----------------------------

- `docker run --name kafka -p 9092:9092
    -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 
    -e KAFKA_ZOOKEEPER_CONNECT=localhost:2181
    -e KAFKA_OFFSET_TOPICS_REPLICATION_FACTOR=1
    confluentinc/cp-kafka`

LISTENERS are what interfaces Kafka binds to. 
ADVERTISED_LISTENERS are how clients can connect.
PLAINTEXT is the security protocol.


Why is Kafka fast (need to explore more):
-----------------------------------------

- Kafka access and stores data sequentially. (new data will always at the end of the file.)
- Zero copy principal.



