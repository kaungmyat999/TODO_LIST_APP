import pika
import json


rabbitmq_host = 'localhost' 
def get_rabbitmq_message(queue_name):
    try:
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=rabbitmq_host))
        channel = connection.channel()

        # Declare the queue if it doesn't exist
        channel.queue_declare(queue=queue_name)

        # Get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            message = body.decode('utf-8')
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)

            return message
        else:
            return None
    except Exception as e:
        return str(e)
    finally:
        connection.close()

def get_message():
    queue_name = 'events'  
    message = get_rabbitmq_message(queue_name)
    if message:
        return (json.loads(message))
        
    
