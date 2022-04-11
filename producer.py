from kafka import KafkaProducer
from random import choice
from config import BOOTSTRAP_SERVER, TOPIC_NAME

producer = KafkaProducer(bootstrap_servers=BOOTSTRAP_SERVER)

send_future = producer.send(
    TOPIC_NAME, 
    b'raw bytes I guess',
    partition=choice([0, 1])
)

record_metadata = send_future.get()

print(record_metadata)