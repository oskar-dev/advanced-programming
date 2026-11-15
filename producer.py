import pika
import json

import argparse

def spawn_task():
    global next_id
    next_id += 1

    payload = {
        'task_id': next_id,
        'status': 'pending'
    }

    channel.basic_publish(exchange='', routing_key='task_queue', body=json.dumps(payload))

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

next_id = 0

channel.queue_declare(queue='task_queue', durable=True)

parser = argparse.ArgumentParser(description='Spawn tasks and send them to the task queue.')
parser.add_argument('--n', type=int, default=1, help='Number of tasks to spawn (default: 1)')
args = parser.parse_args()

for _ in range(args.n):
    spawn_task()

connection.close()
