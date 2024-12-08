import pika

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the same queue (must match producer's queue)
channel.queue_declare(queue='events')

# Define a callback function to process incoming messages
def callback(ch, method, properties, body):
    print(f"[Consumer] Received: {body.decode()}")

# Set up a consumer on the queue
channel.basic_consume(queue='events', on_message_callback=callback, auto_ack=True)

print("[Consumer] Waiting for events. Press CTRL+C to exit.")
channel.start_consuming()