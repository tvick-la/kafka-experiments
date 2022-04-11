from kafka import KafkaAdminClient, admin
from kafka.admin.new_partitions import NewPartitions

from config import BOOTSTRAP_SERVER, TOPIC_NAME

admin_client = KafkaAdminClient(
    bootstrap_servers=BOOTSTRAP_SERVER   
)

new_topics = [
    admin.NewTopic(
        name=TOPIC_NAME, 
        num_partitions=2,
        replication_factor=1
    )
]
print("Desired Topics: ", [topic.name for topic in new_topics])

existing_topics = admin_client.list_topics()
print("Existing Topics:", existing_topics)

topics_to_add = [topic for topic in new_topics if topic.name not in existing_topics]
print("Topics to add:  ", [topic.name for topic in topics_to_add])

admin_client.create_topics(topics_to_add)

existing_topics = admin_client.list_topics()
print("Existing Topics:", existing_topics)

print("\nTopics Created")

admin_client.close()