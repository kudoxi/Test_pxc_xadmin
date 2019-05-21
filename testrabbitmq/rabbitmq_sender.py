
import pika

#用户名和密码
credentials = pika.PlainCredentials('kudoxi','kudoxi')
#连接机器
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.254.138',credentials=credentials
))

#建立rabbitmq协议通道
channel = connection.channel()

#声明队列，告诉要发到哪个队列里
channel.queue_declare(queue='hello')

#发消息
#exchange 交换机
#routing_key
channel.basic_publish(
                    exchange='',
                    routing_key='hello',
                    body='hello world')

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