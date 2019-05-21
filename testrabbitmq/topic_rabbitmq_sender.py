
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

#定义交换机
channel.exchange_declare(exchange='topic_logs',exchange_type='topic')

#log级别
routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'


message = ''.join(sys.argv[2:]) or "hello world! %s" % time()
#发消息
channel.basic_publish(
                    exchange='topic_logs',
                    routing_key=routing_key,
                    body=message,
)

print('[x] sent %r'% message)
#关掉队列
connection.close()


#创建用户
#rabbitmqctl add_user kudoxi kudoxi
#创建管理员
#rabbitmqctl set_user_tags kudoxi administrator
#授权
#rabbitmqctl set_permissions -p / kudoxi ".*" ".*" ".*"
#重启服务
#/etc/init.d/rabbitmq-server restart
#获取消息 sender里面发了，可以用该命令获取
#rabbitmqctl list_queues