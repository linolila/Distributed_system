

---

# Distributed Task and Notification System

## Description

A simple distributed system to demonstrate task assignment and notifications using RabbitMQ and MySQL. The system allows an admin to assign tasks to employees, who then send notifications upon task completion. MySQL is used for persistent storage of tasks and notifications.

## Components

1. **Task Publisher**: Admin sends tasks.
2. **Task Consumer**: Employees receive tasks and mark them as completed.
3. **Notification Publisher**: Employees send task completion notifications.
4. **Notification Consumer**: Admin receives notifications.

## Prerequisites

- Python 3.8 or higher
- RabbitMQ installed and running locally
- MySQL installed and running

## Setup Instructions

### 1. Install Dependencies

First, install the necessary dependencies for Python:

```bash
pip install -r requirements.txt
```

### 2. Install RabbitMQ Locally

#### Install Erlang (a prerequisite for RabbitMQ)

1. Visit the [Erlang/OTP Downloads](https://www.erlang.org/downloads) page.
2. Download and install the version compatible with your operating system.

#### Install RabbitMQ

1. Go to the [RabbitMQ Downloads](https://www.rabbitmq.com/download.html) page.
2. Download the installer for your system (e.g., `.exe` for Windows or package for macOS/Linux).
3. Follow the installation instructions.

#### Enable the RabbitMQ Management Plugin

After RabbitMQ installation, enable the management plugin:

```bash
rabbitmq-plugins enable rabbitmq_management
```

#### Start RabbitMQ

- On **Windows**, start the RabbitMQ service from the **Services** app.
- On **macOS/Linux**, start RabbitMQ with the following command:

```bash
sudo rabbitmq-server
```

#### Access the RabbitMQ Web UI

Open [http://localhost:15672](http://localhost:15672) in your browser. Default login credentials are:

- **Username**: `guest`
- **Password**: `guest`

### 3. Set Up MySQL Database

To store tasks and notifications, set up MySQL:

#### Create the Database and Tables

Run the following SQL commands in your MySQL client (e.g., MySQL Workbench, command line, etc.):

```sql
CREATE DATABASE task_system;

USE task_system;

-- Create table for tasks
CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task_name VARCHAR(255) NOT NULL,
    status ENUM('assigned', 'completed') DEFAULT 'assigned',
    assigned_to VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create table for notifications
CREATE TABLE notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task_id INT,
    notification_message TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(id)
);
```

### 4. Run the System

To run the system, follow these steps:

#### 1. Run Task Publisher

Run the `task_publisher.py` script to send tasks:

```bash
python task_publisher.py
```

You’ll be prompted to enter a task and an employee name. The task will be saved to MySQL and sent to RabbitMQ.

#### 2. Run Task Consumer

Run the `task_consumer.py` script to receive and mark tasks as completed:

```bash
python task_consumer.py
```

Once a task is processed, it will be updated as "completed" in the MySQL database.

#### 3. Run Notification Publisher

Run the `notification_publisher.py` script to send notifications:

```bash
python notification_publisher.py
```

You’ll be prompted to enter the task ID and a notification message. The notification will be saved to MySQL and sent to RabbitMQ.

#### 4. Run Notification Consumer

Run the `notification_consumer.py` script to receive notifications:

```bash
python notification_consumer.py
```

The system will display the received notification and save it to MySQL.

## Notes

Ensure that RabbitMQ is running before starting any script.
```

This markdown format will be ideal for a `README.md` file in your repository.