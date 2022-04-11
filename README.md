# Experimenting with Kafka
Using python, running kafka in docker locally.

### Stand Up a Kafka cluster with docker
```sh
docker-compose up -d
```

Use `docker-compose logs -f` to log, and `docker-compose down` to stop.

### Install Python Kafka requirement
Ideally, you are using some sort of virtual environment.
See [pyenv](https://github.com/pyenv/pyenv) for python version management and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) for creating virtual environments.

```sh
pip install -r requirements
```

### Create a topic
```sh
python create_topics.py
```

### Print kafka broker information
Lists topics, partitions, current end offsets
```sh
python status.py
```

### Consume messages on the topic
Create a consumer and poll for messages.
```sh
python consumer.py
```

You can create multiple consumers, all as part of the same group, and partitions will be assigned to those consumers automatically.  Partition count is set in `create_topics.py`

### Produce messages on the topic
Send a single hard-coded message with each invokation, to a random partition.
```sh
python producer.py
```

### Delete the topic
Clean up your topic and start from scratch.
```sh
python delete_topics.py
```