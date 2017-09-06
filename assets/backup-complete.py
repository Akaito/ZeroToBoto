# backup-complete.py

import os

import boto3
import botocore


#====================================================================
BUCKET_NAME = 'zerotoboto' # (create the bucket first in the AWS GUI)

session = boto3.Session(profile_name='default')
s3 = session.client('s3')
prefix = os.getcwd().split('/')[-1]  # get current folder's name; not all stuff leading to it


for dir_listing in os.walk(os.getcwd()):
    here = dir_listing[0]
    dirnames = dir_listing[1]
    filenames = dir_listing[2]
    # don't upload anything in hidden directories
    # bug: directories inside hidden directories *will* be uploaded
    if here[0] == '.':
        continue

    for filename in filenames:
        if filename[0] == '.':  # don't upload hidden files
            continue
        filename_full = here + '/' + filename
        key = filename_full[len(os.getcwd()):]
        if key[0] == '/':  # cleaner S3 keys on Linux
            key = key[1:]
        key = prefix + '/' + key  # prepend the prefix from the command line arg
        s3.upload_file(filename_full, BUCKET_NAME, key)
        print 'Uploaded {}\n      to {}:{}'.format(filename_full, BUCKET_NAME, key)

