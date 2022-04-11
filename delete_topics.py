from kafka import KafkaAdminClient, admin

from config import BOOTSTRAP_SERVER, TOPIC_NAME

admin_client = KafkaAdminClient(
    bootstrap_servers=BOOTSTRAP_SERVER   
)

existing_topics = admin_client.list_topics()
print("Existing Topics:", existing_topics)

print("Deleting topics...")
topics_to_be_gone = [TOPIC_NAME]
topics_to_delete = [topic for topic in topics_to_be_gone if topic in existing_topics]
admin_client.delete_topics(topics_to_delete)

existing_topics = admin_client.list_topics()
print("Existing Topics:", existing_topics)
