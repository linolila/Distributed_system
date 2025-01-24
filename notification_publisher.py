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
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Send a notification to RabbitMQ
task_id = input("Enter the task ID: ")
notification_message = input("Enter notification message: ")

# Insert notification into MySQL
cursor.execute("INSERT INTO notifications (task_id, notification_message) VALUES (%s, %s)", (task_id, notification_message))
db.commit()

# Send notification to RabbitMQ
channel.queue_declare(queue='notification_queue')
channel.basic_publish(exchange='', routing_key='notification_queue', body=notification_message)

print(f"Notification for task {task_id} sent.")

# Close connections
cursor.close()
db.close()
connection.close()

# import pika

# def publish_notification(notification_message):
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()
#     channel.queue_declare(queue='notification_queue')
#     channel.basic_publish(exchange='', routing_key='notification_queue', body=notification_message)
#     print(f"Notification sent: {notification_message}")
#     connection.close()

# if __name__ == "__main__":
#     notification = input("Enter a completion notification: ")
#     publish_notification(notification)