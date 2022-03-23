#!/usr/bin/env python
import pika
import time
from speechText import speechToText

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)
print('Waiting for messages to queue. CTRL+C will exit')


def callback(ch, method, properties, body):
    print("Received %r" % body.decode())
    speechToText(body)
    print("Job Done")

    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='task_queue', on_message_callback=callback)

channel.start_consuming()