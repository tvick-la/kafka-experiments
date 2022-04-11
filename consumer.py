from kafka import KafkaConsumer

from config import BOOTSTRAP_SERVER, TOPIC_NAME

consumer = KafkaConsumer(
    group_id='arbitrary',
    bootstrap_servers=BOOTSTRAP_SERVER
)

try:
    consumer.subscribe(TOPIC_NAME)
    while True:
        msg = consumer.poll(timeout_ms=1000)
        if msg is not None: 
            print(msg)
finally:
    print('closing')
    consumer.close()