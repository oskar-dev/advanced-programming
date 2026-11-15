import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue', durable=True)

def callback(ch, method, properties, body):
    print(f"Received task: {body.decode()}")

channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)
channel.start_consuming()

connection.close()