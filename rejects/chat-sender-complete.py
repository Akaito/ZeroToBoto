# chat-receiver-complete.py

import boto3


#====================================================================


#====================================================================
session = boto3.Session(profile_name='awsday-admin')
sqs = session.resource('sqs')
QUEUE_NAME = 'sqsq-chris-zerotoboto-chat.fifo'

queue = sqs.get_queue_by_name(QueueName=QUEUE_NAME)
print queue.attributes
exit()

user_input = ''
while user_input not in ('quit', 'exit'):
    user_input = raw_input('> ')
    response = queue.send_message(MessageBody=user_input, MessageGroupId='1')

