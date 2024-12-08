import pika
import time

# Establish connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare a queue
channel.queue_declare(queue='events')

# Send messages to the queue
for i in range(10):
    message = f"Event {i+1}: Hello, World!"
    channel.basic_publish(exchange='', routing_key='events', body=message)
    print(f"[Producer] Sent: {message}")
    time.sleep(1)  # Simulate time delay between events

# Close the connection
connection.close()
