# backup-complete.py

import os

import boto3
import botocore


#====================================================================
BUCKET_NAME = 'zerotoboto' # (create the bucket first in the AWS GUI)

session = boto3.Session(profile_name='default')
s3 = session.client('s3')
prefix = os.getcwd().split('/')[-1]  # get current folder's name; not all stuff leading to it


# visit the current directory and every one within it, recursively
for dir_listing in os.walk(os.getcwd()):
    here = dir_listing[0]  # full path 'here' for this iteration of the loop
    dirnames = dir_listing[1]  # list of directories here
    filenames = dir_listing[2]  # list of files here

    # don't upload anything in hidden directories
    # bug: directories inside hidden directories *will* be uploaded
    # extra credit: fix that bug  :)
    if here[0] == '.':
        continue

    for filename in filenames:
        # don't upload hidden files
        if filename[0] == '.':
            continue

        # absolute, full path to the file on disk
        file_abspath = here + '/' + filename
        # S3 object key
        key = file_abspath[len(os.getcwd()):]
        if key[0] == '/':  # cleaner S3 keys on Linux
            key = key[1:]  # remove leading slash
        # prepend the prefix so files aren't all dumped straight into bucket root
        key = prefix + '/' + key

        # extra credit: check the hash of the object in S3, and don't upload if the local file is the same.
        # easier way: check modtime of file in S3 versus modtime on disk.
        # extra credit: sync mode; *download* file if its modtime is newer and hashes differ
        s3.upload_file(file_abspath, BUCKET_NAME, key)
        print 'Uploaded {}\n      to {}:{}'.format(file_abspath, BUCKET_NAME, key)

