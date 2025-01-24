# Distributed Task System

## Description
A simple distributed system to demonstrate task assignment and notifications using RabbitMQ.

## Components
1. **Task Publisher**: Admin sends tasks.
2. **Task Consumer**: Employees receive tasks.
3. **Notification Publisher**: Employees send task completion notifications.
4. **Notification Consumer**: Admin receives notifications.


## Prerequisites

- Python 3.8 or higher
- RabbitMQ installed and running locally

## Setup Instructions

### 1. Install Dependencies

First, install the necessary dependencies:

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

After RabbitMQ installation, enable the management plugin with the following command:

```bash
rabbitmq-plugins enable rabbitmq_management
```

#### Start RabbitMQ

- On **Windows**, start the RabbitMQ service from the **Services** app.
- On **macOS/Linux**, use the following command to start RabbitMQ:

```bash
sudo rabbitmq-server
```

#### Access the RabbitMQ Web UI

Open [http://localhost:15672](http://localhost:15672) in your browser. The default login credentials are:
- **Username**: `guest`
- **Password**: `guest`

## Running the System

To run the system, follow these steps:

### 1. Run Task Publisher

Run the `task_publisher.py` script to send tasks:

```bash
python task_publisher.py
```

You’ll be prompted to enter a task to send.

### 2. Run Task Consumer

Run the `task_consumer.py` script to receive the task:

```bash
python task_consumer.py
```

You’ll be able to view the task that was received.

### 3. Run Notification Publisher

Run the `notification_publisher.py` script to send notifications:

```bash
python notification_publisher.py
```

Enter a notification to send when prompted.

### 4. Run Notification Consumer

Run the `notification_consumer.py` script to view received notifications:

```bash
python notification_consumer.py
```

The system will display the notification received.

## Notes

Ensure that RabbitMQ is running before starting any script.
```

This markdown format will be ideal for a `README.md` file in your repository.