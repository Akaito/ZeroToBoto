---
category: info
info_order: 6
date: 2017-09-05 00:25 -07:00
title: Backup to S3
---

```
chris@CSU:~/work/ZeroToBoto/assets$ python backup-complete.py
Uploaded /home/chris/work/ZeroToBoto/assets/rpg-3.py
      to zerotoboto:assets/rpg-3.py
Uploaded /home/chris/work/ZeroToBoto/assets/hangman-0.py
      to zerotoboto:assets/hangman-0.py
Uploaded /home/chris/work/ZeroToBoto/assets/css/style.scss
      to zerotoboto:assets/css/style.scss
```

<!-- more -->


## Prerequisites

1. Create a free AWS account [here](https://aws.amazon.com/free/).
1. Create IAM access key/secret and store them in a *credentials* file for command-line use, as described [here](http://docs.aws.amazon.com/cli/latest/userguide/cli-config-files.html).
1. `pip install boto3`.  See [here](https://boto3.readthedocs.io/en/latest/guide/quickstart.html) for more.  You'll use boto3 whether you're using Python 2 or Python 3.
	On that "quickstart" page linked in this step, try just the first little bit up to listing buckets.
1. Create an S3 bucket in AWS using the [Web GUI](https://s3.console.aws.amazon.com/s3/home).


## Walking the local filesystem

Python's <tt>os</tt> module has some very handy functions like <tt>[walk()](https://docs.python.org/2/library/os.html#os.walk)</tt> and <tt>[getcwd()](https://docs.python.org/2/library/os.html#os.getcwd)</tt> that will be extremely useful.

```python
>>> import os
>>> os.getcwd()
'/home/chris/work/ZeroToBoto/assets'
>>> 
>>> for thing in os.walk(os.getcwd()):
...     print thing  # what does os.getcwd() give us?
... 
('/home/chris/work/ZeroToBoto/assets', ['css'], ['.backup-complete.py.swp', 'rpg-3.py', 'message-board-complete.py', 'hangman-0.py', 'hangman-complete.py', 'rpg-1.py', 'guessing-game-0.py', 'guessing-game-2.py', 'guessing-game-complete.py', 'rpg-2.py', 'guessing-game-1.py', 'adventure-complete.py', 'adventure-1.py', 'hello-python-complete.py', 'adventure-0.py', 'hangman-dictionary.txt', 'rpg-0.py', 'hangman-2.py', 'backup-complete.py', 'hangman-3.py', 'hangman-1.py', 'rpg-4.py', 'rpg-complete.py', 'echo-server-complete.py'])
('/home/chris/work/ZeroToBoto/assets/css', [], ['style.scss'])
>>> 
>>> for contents in os.walk(os.getcwd()):
...     for filename in contents[2]:
...             print filename
... 
.backup-complete.py.swp
rpg-3.py
message-board-complete.py
hangman-0.py
hangman-complete.py
rpg-1.py
style.scss
# (and so on)
```

`os.getcwd()` returns a string that is your **c**urrent **w**orking **d**irectory.

Each time `os.walk(<dir>)` is called in a loop, it returns a tuple of lists.
(A tuple is basically a fixed-size list.)
The tuple's first item (at index 0) is the location you're currently looking at.
The second item (index 1) is a list of folders in your current location.
The third and final is a list of files in your current location.
Be mindful of relative vs. absolute paths.
Each iteration of a loop involving os.walk() will give filenames relative to the directory it's currently looking at.
Not relative to where you started from, and not absolute.


## Exercise: Printing full paths to files, recursively

```python
chris@CSU:~/work/ZeroToBoto/assets$ python backup-0.py 
/home/chris/work/ZeroToBoto/assets/rpg-3.py
/home/chris/work/ZeroToBoto/assets/hangman-0.py
/home/chris/work/ZeroToBoto/assets/css/style.scss
```

Print out the absolute path to every file in the current working directory and below, recursively.
Do *not* print directory names on their own.
Just files.

Note that style.scss is in the css directory, below where the script is being run from.
There's also a lot of output that I'm cutting from the examples to keep things concise.

Part of the exercise is also to skip "dotfiles", a common type of hidden file in \*nix systems.
That's just any file whose name begins with a period.

### Hints

1. You'll need to add strings together.
	Since Windows and \*nix OSes both understand the forward slash as a directory separator, feel free to just use that for formatting your paths.
2. An earlier show of os.walk() in this page will get you halfway there.


## Preparing to upload


[Boto3 S3 docs](http://boto3.readthedocs.io/en/latest/reference/services/s3.html)

[Boto3 S3 examples](http://boto3.readthedocs.io/en/latest/reference/services/s3.html#examples)


[SQS tutorial](http://boto3.readthedocs.io/en/latest/guide/sqs.html)

