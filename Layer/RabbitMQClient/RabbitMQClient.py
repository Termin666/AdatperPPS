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
        self.channel.exchange_declare(exchange='rating_exchange', exchange_type='topic', durable=False)
        print("Connection to RabbitMQ established")

    def add_topic(self, routing_key, handler_class: MessageHandlerInterface):
        queue_name = f"{routing_key}_queue"
        self.topics[routing_key] = handler_class
        self.channel.queue_declare(queue=queue_name, durable=False)
        self.channel.queue_bind(queue=queue_name, exchange='rating_exchange', routing_key=routing_key)

        self.channel.basic_consume(queue=queue_name, on_message_callback=self.topics[routing_key].handle_message, auto_ack=True)

        print(f"Subscribed to routing_key: {routing_key}")

    def start_consuming(self):
        print("Starting to consume messages")
        self.channel.start_consuming()

    def stop(self):
        if self.connection:
            self.connection.close()
            print("Connection to RabbitMQ closed")