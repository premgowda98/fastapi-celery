## Async Task Processing

1. FastAPI as Websever
2. Celery as Task Queue
3. RabbitMQ as Message Broker
4. Flower to monitor celery workers

### Setup

1. Intsall rabbitmq `docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4.0-management`
2. Start celery `celery -A tasks worker --loglevel=info`
3. Start flower `celery -A tasks flower --loglevel=info`
4. Start Webserver
5. Redis as backend `docker run -d --name redis -p 6379:6379 redis` and also `pip install redis`

### Celery

1. Backend is where the state is preservered, it can be redis or any other RDBMS
2. Delay vs Async_run, the latter has more functionality
3. .delay() return the id of the task
4. .get() is a blocing operation which waits for task to compelet

