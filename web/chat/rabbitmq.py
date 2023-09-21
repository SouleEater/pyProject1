# rabbitmq.py

import pika
from django.conf import settings

def send_to_rabbitmq(message):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=settings.RABBITMQ_HOST,
            port=settings.RABBITMQ_PORT,
            virtual_host=settings.RABBITMQ_VIRTUAL_HOST,
            credentials=pika.PlainCredentials(
                settings.RABBITMQ_USERNAME, settings.RABBITMQ_PASSWORD
            )
        ))
        channel = connection.channel()
        channel.queue_declare(queue='chat_queue')
        channel.basic_publish(exchange='', routing_key='chat_queue', body=message)
        connection.close()
    except Exception as e:
        print(f"Error sending message to RabbitMQ: {e}")
