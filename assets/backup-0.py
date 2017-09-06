# backup-0.py

import os


#====================================================================
# visit the current directory and every one within it, recursively
for dir_listing in os.walk(os.getcwd()):
    here = dir_listing[0]  # full path 'here' for this iteration of the loop
    dirnames = dir_listing[1]  # list of directories here
    filenames = dir_listing[2]  # list of files here

    for filename in filenames:
        # don't upload hidden files
        if filename[0] == '.':
            continue

        # absolute, full path to the file on disk
        file_abspath = here + '/' + filename
        print file_abspath

