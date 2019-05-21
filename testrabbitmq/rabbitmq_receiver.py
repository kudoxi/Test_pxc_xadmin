import pika
from time import sleep
#用户名和密码
credentials = pika.PlainCredentials('kudoxi','kudoxi')
#连接机器
connection = pika.BlockingConnection(pika.ConnectionParameters(
    '192.168.254.138',credentials=credentials
))

#建立rabbitmq协议通道
channel = connection.channel()


#声明队列，从哪里接收
channel.queue_declare(queue='hello')


#ch 通道channel的实例
def callback(ch,method,properties,body):
    print("start processing ... ")
    sleep(20)
    print('[x] Receive %r'%ch,method,properties,body)

#从队列拿到数据后调取callback---注意，不同版本，参数位置不一样
channel.basic_consume("hello",callback)#,no_ack=True

#开始消费
print('[*]waiting for messages.To exit press ctrl+c')
channel.start_consuming()