# chat-receiver-complete.py

import random
import string

import boto3


#====================================================================
session = boto3.Session(profile_name='awsday-admin')

sns = session.resource('sns')
topic = sns.Topic('arn:aws:sns:us-east-1:615783546267:snstopic-chris-zerotoboto-chat')


#sqs = session.client('sqs')  # nope!
sqs = session.resource('sqs')
QUEUE_NAME_FORMAT = 'sqsq-chris-zerotoboto-chat-{}.fifo'

random_str = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(12))
queue_name = QUEUE_NAME_FORMAT.format(random_str)

# need a queue per listener to the topic, so it can handle message visibility/deletion
queue = sqs.create_queue(QueueName=queue_name, Attributes={
    'FifoQueue': 'true',
    'DelaySeconds': '0',
    'ReceiveMessageWaitTimeSeconds': '20'
    })


# subscribe SQS queue to SNS topic
sub_response = topic.subscribe(Protocol='sqs', Endpoint=queue.attributes['QueueArn'])
print sub_response
print dir(sub_response)
queue.delete()
exit()


while True:
    for message in queue.receive_messages():
        print message.body
        message.delete()
        if message.body == 'end':
            queue.delete()
            break

