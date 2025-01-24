import pika

def consume_notifications():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notification_queue')

    def callback(ch, method, properties, body):
        print(f"Notification received: {body.decode()}")

    channel.basic_consume(queue='notification_queue', on_message_callback=callback, auto_ack=True)
    print("Waiting for notifications...")
    channel.start_consuming()

if __name__ == "__main__":
    consume_notifications()