import pika
from Layer.MessageHandlers.MessageHandlerInterface import MessageHandlerInterface


class RabbitMQClient:
    def __init__(self, host='localhost'):
        self.host = host
        self.connection = None
        self.channel = None
        self.topics = {}

    def start(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.host))
        self.channel = self.connection.channel()
        print("Connection to RabbitMQ established")

    def add_topic(self, topic, handler_class: MessageHandlerInterface):

        self.topics[topic] = handler_class
        self.channel.queue_declare(queue=topic)
        self.channel.basic_consume(queue=topic, on_message_callback=self.topics[topic].handle_message, auto_ack=True)
        print(f"Subscribed to topic: {topic}")

    def start_consuming(self):
        print("Starting to consume messages")
        self.channel.start_consuming()

    def stop(self):
        if self.connection:
            self.connection.close()
            print("Connection to RabbitMQ closed")
