import pika
import json



def sendMessage():
    event_data = {
        'event' : 'Congratulations You Finished All!!!'
    }

    # Establish a connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare a queue for the event
    channel.queue_declare(queue='events')

    # Publish the event to the 'events' queue
    channel.basic_publish(exchange='', routing_key='events', body=json.dumps(event_data))

    # Close the connection
    connection.close()

