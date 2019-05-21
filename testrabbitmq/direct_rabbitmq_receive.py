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

#建立交换机
channel.exchange_declare(exchange='direct_logs',exchange_type='direct')

#声明队列
result = channel.queue_declare(queue='',exclusive=True)
#不指定队列名，rabbit会随机分配一个名字
#exclusive=True会在消费者断开队列后，自动删除这个队列
quename = result.method.queue


#级别-必须给传入的消息绑定级别分类
serverities = sys.argv[1:]
if not serverities:
    sys.stderr.write("Usage :%s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)

for servrity in serverities:
    # 有多少级别，就循环绑定到交换机上
    channel.queue_bind(
        exchange='direct_logs',
        queue=quename,
        routing_key=servrity
    )

print("[*] waiting for logs.")

def callback(ch,method,properties,body):
    print("[x] %r %r" % (method.routing_key,body))

channel.basic_consume(quename,callback,auto_ack=False)

#开始消费
print('[*]waiting for messages.To exit press ctrl+c')
channel.start_consuming()