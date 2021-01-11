# Stock News Summarizer
Side Project

<h3>How to test Kafka</h3>
<p>
1. Run <code>docker-compose up</code>
<br>
2. Run <code>docker exec -it kafka /bin/bash</code>
<br>
3. Check the topic to test exists by running
<code>sh /opt/kafka_2.13-2.7.0/bin/kafka-topics.sh --zookeeper zookeeper --list</code>
<br>
4. Run <code>sh /opt/kafka_2.13-2.7.0/bin/kafka-console-producer.sh --topic={topic name} --broker-list=kafka:9092</code>
<br>
5. Write some messages
<br>
6. Run <code>sh /opt/kafka_2.13-2.7.0/bin/kafka-console-consumer.sh --topic={topic name} --bootstrap-server=kafka:9092 --from-beginning</code>
</p>