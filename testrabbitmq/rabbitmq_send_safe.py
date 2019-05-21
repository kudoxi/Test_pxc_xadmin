#可以安全处理消息
import pika
import sys
from time import time

#用户名和密码
credentials = pika.PlainCredentials('kudoxi','kudoxi')
#连接机器
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.254.138',credentials=credentials
))

#建立rabbitmq协议通道
channel = connection.channel()
#声明队列，告诉要发到哪个队列里
channel.queue_declare(queue='task_queue',durable=True)
#durable :队列持久化，重启服务后，队列依然存在，但是里面的消息没有了

message = ''.join(sys.argv[1:]) or "hello world! %s" % time()
#发消息
channel.basic_publish(
                    exchange='',
                    routing_key='task_queue',
                    body=message,
                    properties=pika.BasicProperties(
                        delivery_mode=2, #消息持久化
                    )
)
#properties消息持久化

print('[x] sent %r'% message)
#关掉队列
connection.close()
