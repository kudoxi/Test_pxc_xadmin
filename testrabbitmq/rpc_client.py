import pika
import uuid

#斐波那契客户端（发送方）
class FibonacciRpcClient(object):
    def __init__(self):
        credentials = pika.PlainCredentials('kudoxi', 'kudoxi')
        # 连接机器
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(
            '192.168.254.138', credentials=credentials
        ))
        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue='', exclusive=True)
        self.callback_queue = result.method.queue
        #准备接收结果
        self.channel.basic_consume(self.callback_queue, self.on_response, auto_ack=False)

    #回调
    def on_response(self,ch,method,properties,body):
        #检查唯一标识符和发送时是不是同一个
        if self.corr_id == properties.correlation_id:
            self.response = body

    def call(self,n):
        self.response = None
        self.corr_id = str(uuid.uuid4())
        # 发消息
        self.channel.basic_publish(
            exchange='',
            routing_key='rpc_queue',
            properties = pika.BasicProperties(
                reply_to=self.callback_queue, #服务端回复到哪个队列
                correlation_id=self.corr_id#命令发送和回复的唯一标识
            ),
            body=str(n),
        )

        #结果接收
        while self.response is None:

            self.connection.process_data_events()#检查队列是否有新消息，不会阻塞（原start_comsuming会一直阻塞等待）


        return int(self.response)

fibonacci_rpc = FibonacciRpcClient()
print('[x] Requesting fib(30)')
response = fibonacci_rpc.call(30)
print('[.] GOT %r '%response)