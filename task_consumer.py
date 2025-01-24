import pika

def consume_tasks():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue')

    def callback(ch, method, properties, body):
        print(f"Received task: {body.decode()}")

    channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)
    print("Waiting for tasks...")
    channel.start_consuming()

if __name__ == "__main__":
    consume_tasks()