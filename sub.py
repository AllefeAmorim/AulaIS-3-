from __future__ import print_function
from is_wire.core import Channel, Subscription, Message
import time

# Connect to the broker
channel = Channel("amqp://guest:guest@10.10.0.91:5672")

# Subscribe to the desired topic(s)
subscription = Subscription(channel)
subscription.subscribe(topic="Aluno.Joab")
# ... subscription.subscribe(topic="Other.Topic")
message = Message()
message.reply_to = "Joab"

while True:

    msg = input("Escreva a msg: ")
    dest = input("Destino: ")
    message.body = msg.encode('utf-8')
    channel.publish(message, topic=f"Aluno.{dest}")
    message = channel.consume()
    user = message.reply_to

    print(f'{user} : {message.body.decode()}')
    time.sleep(1)
