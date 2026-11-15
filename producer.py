import pika

import json

from fastapi import FastAPI

app = FastAPI()

next_id = 0

@app.post("/analyze_img/{img_url}")
def analyze_img(img_url: str):
    global next_id

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='images', durable=True, arguments={"x-queue-type": "quorum"})

    payload = {
        "id": next_id,
        "img_url": img_url
    }

    channel.basic_publish(exchange='', routing_key='images', body=json.dumps(payload))

    next_id += 1

    connection.close()