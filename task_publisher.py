import pika

def publish_task(task_description):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='task_queue')
    channel.basic_publish(exchange='', routing_key='task_queue', body=task_description)
    print(f"Task sent: {task_description}")
    connection.close()

if __name__ == "__main__":
    task = input("Enter a task to assign: ")
    publish_task(task)