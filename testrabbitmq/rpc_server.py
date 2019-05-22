import pika
import time

credentials = pika.PlainCredentials('kudoxi','kudoxi')
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.254.138',credentials=credentials
))
channel = connection.channel()


channel.queue_declare(queue='rpc_queue')

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch,method,properties,body):
    n = int(body)

    print('[.]fib(%s)'%n)

    response = fib(n)

    #把结果返回给客户端
    ch.basic_publish(
        exchange='',
        routing_key=properties.reply_to,
        properties = pika.BasicProperties(
            correlation_id=properties.correlation_id,
        ),
        body = str(response)
    )
    #确认完成
    ch.basic_ack(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)#一次只处理一个任务
channel.basic_consume("rpc_queue",on_request)#接收客户端发来的任务，调用回调函数

print('[x] Awaiting RPC requests')
channel.start_consuming()