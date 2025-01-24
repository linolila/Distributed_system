import mysql.connector
import pika

# Connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",  # change to your MySQL username
    password="password",  # change to your MySQL password
    database="task_system"
)
cursor = db.cursor()

# Connect to RabbitMQ
def callback(ch, method, properties, body):
    notification_message = body.decode()
    print(f"Received notification: {notification_message}")

    # Insert the notification into MySQL
    cursor.execute("INSERT INTO notifications (notification_message) VALUES (%s)", (notification_message,))
    db.commit()

# Set up RabbitMQ consumer
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='notification_queue')
channel.basic_consume(queue='notification_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for notifications...')
channel.start_consuming()

# Close connections (never reached if the consumer is running indefinitely)
cursor.close()
db.close()

# import pika

# def consume_notifications():
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()
#     channel.queue_declare(queue='notification_queue')

#     def callback(ch, method, properties, body):
#         print(f"Notification received: {body.decode()}")

#     channel.basic_consume(queue='notification_queue', on_message_callback=callback, auto_ack=True)
#     print("Waiting for notifications...")
#     channel.start_consuming()

# if __name__ == "__main__":
#     consume_notifications()