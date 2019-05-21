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
channel.queue_declare(queue='task_queue',durable=True)
#send里面已经设置为了持久化，这里声明队列也必须设置为持久化，队列一旦声明就不能再更改


#ch 通道channel的实例
def callback(ch,method,properties,body):
    print("start processing ... %r"%body)
    sleep(20)
    print("[x] done ")
    print("[x] message.delivery_tag ",method.delivery_tag)
    ch.basic_ack(delivery_tag=method.delivery_tag)#发送一个随机值，作为响应标记符

#从队列拿到数据后调取callback---注意，不同版本，参数位置不一样
channel.basic_consume("task_queue",callback,auto_ack=False)
#auto_ack 是否给队列发送标识符标识自己已经接收，如果是TRUE，那么会自动发送，即使中断了，队列中的消息也被拿走了
#如果是false，中断之后，队列中的消息还在，一定要完整执行结束，消息才会被释放

#开始消费
print('[*]waiting for messages.To exit press ctrl+c')
channel.start_consuming()