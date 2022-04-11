from kafka import KafkaAdminClient, KafkaConsumer
from kafka.structs import TopicPartition
from config import BOOTSTRAP_SERVER


admin_client = KafkaAdminClient(bootstrap_servers=BOOTSTRAP_SERVER)
consumer = KafkaConsumer(
    group_id='arbitrary',
    bootstrap_servers=BOOTSTRAP_SERVER
)

print("TOPICS:")
topics = admin_client.list_topics()
print(topics)

print("PARTITIONS")
for topic in (topic for topic in topics if '__' not in topic):
    partitions = consumer.partitions_for_topic(topic)
    print(topic, partitions)
    for partition in partitions:
        end_offsets = consumer.end_offsets([TopicPartition(topic, partition)])
        end_offset = list(end_offsets.values())[0]
        print(topic, partition, end_offset)

consumer.close()
admin_client.close()