# backup-1.py

import os


#====================================================================
cwd = os.getcwd()
prefix = cwd.split('/')[-1]  # get current folder's name; not all stuff leading to it


# visit the current directory and every one within it, recursively
for dir_listing in os.walk(cwd):
    here = dir_listing[0]  # full path 'here' for this iteration of the loop
    dirnames = dir_listing[1]  # list of directories here
    filenames = dir_listing[2]  # list of files here

    for filename in filenames:
        # don't upload hidden files
        if filename[0] == '.':
            continue

        # absolute, full path to the file on disk
        file_abspath = here + '/' + filename
        # S3 object key
        key = file_abspath[len(cwd):]
        if key[0] == '/':  # cleaner S3 keys on Linux
            key = key[1:]  # remove leading slash
        # prepend the prefix so files aren't all dumped straight into bucket root
        key = prefix + '/' + key

        print key

