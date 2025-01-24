import pika

def publish_notification(notification_message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notification_queue')
    channel.basic_publish(exchange='', routing_key='notification_queue', body=notification_message)
    print(f"Notification sent: {notification_message}")
    connection.close()

if __name__ == "__main__":
    notification = input("Enter a completion notification: ")
    publish_notification(notification)