# message-board-complete.py

import boto3


#====================================================================
# https://docs.python.org/2.7/library/stdtypes.html#bltin-file-objects
class S3Str(object):
    def __init__(self, s=b''):
        self.s = s

    def read(self, size_bytes=0):
        # important!  read() may be called extra times; head size_bytes!
        # TODO : Implement cursor
        return self.s[:size_bytes]

    def write(self, s):
        self.s += s

    def __str__(self):
        return self.s


#====================================================================
session = boto3.Session(profile_name='awsday-admin')
s3 = session.client('s3')
BUCKET_NAME = 'chrisb-zerotoboto-chat'
BOARD_NAME = 'test'


s = S3Str()
s3.download_fileobj(BUCKET_NAME, BOARD_NAME, s)
if len(s.s) > 0:
    print s

i = raw_input('Say something: ').encode('ascii')
if len(i) > 0 and i.lower() not in ['quit', 'q', 'exit']:
    s.write(b'\n' + i)
    s3.upload_fileobj(s, BUCKET_NAME, BOARD_NAME)
