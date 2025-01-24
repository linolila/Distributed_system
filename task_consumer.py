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
    task_name = body.decode()
    print(f"Received task: {task_name}")

    # Mark the task as completed in MySQL
    cursor.execute("UPDATE tasks SET status = 'completed' WHERE task_name = %s", (task_name,))
    db.commit()

    print(f"Task '{task_name}' marked as completed")

# Set up RabbitMQ consumer
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='task_queue')
channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)

print('Waiting for tasks...')
channel.start_consuming()

# Close connections (never reached if the consumer is running indefinitely)
cursor.close()
db.close()

# import pika

# def consume_tasks():
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()
#     channel.queue_declare(queue='task_queue')

#     def callback(ch, method, properties, body):
#         print(f"Received task: {body.decode()}")

#     channel.basic_consume(queue='task_queue', on_message_callback=callback, auto_ack=True)
#     print("Waiting for tasks...")
#     channel.start_consuming()

# if __name__ == "__main__":
#     consume_tasks()