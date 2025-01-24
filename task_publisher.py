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

# Create task table if not exists
cursor.execute("CREATE TABLE IF NOT EXISTS tasks (id INT AUTO_INCREMENT PRIMARY KEY, task_name VARCHAR(255), status ENUM('assigned', 'completed') DEFAULT 'assigned', assigned_to VARCHAR(255), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)")

# Publish a task to RabbitMQ
task_name = input("Enter task name: ")
assigned_to = input("Enter employee name: ")

# Insert the task into MySQL
cursor.execute("INSERT INTO tasks (task_name, assigned_to) VALUES (%s, %s)", (task_name, assigned_to))
db.commit()

# Send task to RabbitMQ
channel.queue_declare(queue='task_queue')
channel.basic_publish(exchange='', routing_key='task_queue', body=task_name)

print(f"Task '{task_name}' assigned to {assigned_to}")

# Close connections
cursor.close()
db.close()
connection.close()

# import pika

# def publish_task(task_description):
#     connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
#     channel = connection.channel()
#     channel.queue_declare(queue='task_queue')
#     channel.basic_publish(exchange='', routing_key='task_queue', body=task_description)
#     print(f"Task sent: {task_description}")
#     connection.close()

# if __name__ == "__main__":
#     task = input("Enter a task to assign: ")
#     publish_task(task)