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

---

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
The tuple's first item (at index 0) is the absolute path of where you're currently looking.
The second item (index 1) is a list of folder names in your current location.
The third and final is a list of file names in your current location.
Be mindful of relative vs. absolute paths.
Each iteration of a loop involving os.walk() will give filenames relative to the directory it's currently looking at.
Not relative to where you started from, and not absolute.
Only the tuple's first item (index 0) is an absolute path.

---

## Exercise: Printing full paths to files, recursively

```
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

[A completed example.]({{ site.baseurl }}/assets/backup-0.py)

---

## S3 structure

S3 is made up of buckets, and objects within them.
Buckets are effectively unlimited object stores (you can create 100 buckets without asking AWS customer service for more).
An object in S3 is like a key-value pair in a dictionary.
The key is some string, and the value is the binary object (often a file) that you've stored there.
In the Web GUI S3 may look like it's closer to a filesystem with directories and such, but it's just a GUI nicety.
If you give an object a key of "some/path-like/stuff/song.mp3" it'll appear in the GUI to be a few folders down.
But, buckets are flat storage; that whole string is the object's *key*.
You'll also see the term "prefix" used.
A prefix might be something like "music/\*" to refer to all objects whose keys begin with "music/" and have other stuff after that.
It *feels* like it's a directory that you're targeting, but it's slightly different.
Thankfully, we can take advantage of that Web GUI feature to make the backup script's results a little easier to look at there.

---

## Slicing

Python supports a powerful "array slicing" feature.
This can also be applied to strings and other sequences.

```python
>>> s = 'hello'
>>> s[1:]
'ello'
>>> 'hello'[1:]
'ello'
>>> s[:1]
'h'
>>> s[:-1]
'hell'
>>> s[-1:]
'o'
>>> s[len('abc'):]
'lo'
>>> s[1:3]
'el'
```

To slice, act as if you were going to index an array, but then give two indices separated by a colon instead of just one index.
What Python gives you back is the sequence from "begin" (the first index) to "one before end", where "end" is the second index.
Note that "begin" is inclusive, while "end" is exclusive.
This is another one of those things that's a little weird to get used to at first, but makes more sense the deeper you go in programming.
It's a very common way of defining ranges in different languages.

If the begin index is missing, it's implied to be 0 (no effect, since that's inclusive).
If the end index is missing, it's implied to be the sequence's length.
Again no effect, since `'hi'[:len('hi')] == 'hi'[:2]`, and that exclusive end index "2" is one past the index of the last element ('i').
You can also supply both indices.
Supplying neither index (`'hello'[:]`) is a Python-specific trick; it gives you a copy of the sequence back.

When a sequence index is negative, it begins from the end instead of the beginning.
So a sequence's end-minus-one is the last element.
`'hello'[-1] == 'hello'[len('hello')-1]` (recall the "end exclusive" behavior described earlier).

---

## Exercise: Preparing S3 object keys for local files

```
chris@CSU:~/work/ZeroToBoto/assets$ python backup-1.py 
rpg-3.py
hangman-0.py
css/style.scss
```

The script is going to take whatever your current folder is, and basically copy that up to S3.
So in addition to the absolute paths from the last exercise (to refer to the files on disk for uploading), we'll need a place to put things in S3.
Instead of printing those absolute paths, print paths to all files recursively, relative to the current working directory.
So in the example here, <tt>rpg-3.py</tt> is in the <tt>~/work/ZeroToBoto/assets</tt> directory.

If Windows is giving you backslashes (<tt>'\\\\'</tt>), you can use `somestr = somestr.replace('\\', '/')` to make them more widely-accepted forward-slashes.


### Hints

<ol>
<li>The order in which os.walk() advances isn't guaranteed.
	Don't try to build up a path over time as if you were walking down and up directories in order.</li>
<li>Recall that the current walk directory (<tt>tuple[0]</tt>) is the only absolute path.
	Everything else is relative to it.</li>
<li>You'll want to slice off part of the absolute path you have available to create the key.
	But how much?  We want this script to be able to be run from anywhere, so don't cheat and hardcode anything!</li>
{% include spoiler-hint.html major=1 minor=4
	summary="os.getcwd()"
	details="
		os.getcwd() is where you ran the script from, which is what's of interest.
" %}
{% include spoiler-hint.html major=1 minor=5
	summary="len()"
	details="
		You can slice using the len() of a string.  Specifically, os.getcwd().
" %}
</ol>

[A completed example.]({{ site.baseurl }}/assets/backup-1.py)

---

## String splitting

```python
>>> s = 'hi there, this is a test'
>>> s.split(' ')
['hi', 'there,', 'this', 'is', 'a', 'test']
>>> s.split(',')
['hi there', ' this is a test']
```

Another handy feature of Python is its <tt>str</tt> class' <tt>[split()](https://docs.python.org/2/library/stdtypes.html?highlight=str%20split#str.split)</tt> method.
This is especially useful for breaking up paths.

---

## Exercise: Prefix improvement

```
chris@CSU:~/work/ZeroToBoto/assets$ python backup-2.py 
assets/rpg-3.py
assets/hangman-0.py
assets/css/style.scss
```

To make it easier to re-use a bucket and not mix up files from multiple runs of this script, each object uploaded will use a single prefix in common.
Add the name of the current working directory as that prefix.
So, prepend "&lt;cwd&gt;/" to the start of each of the keys you printed above.


### Hints

1. String splitting is useful here.
2. As is a negative index into an array.  Or `len()-1`.

[A completed example.]({{ site.baseurl }}/assets/backup-2.py)

---

## Boto3

The boto module takes some getting used to, and its [documentation](http://boto3.readthedocs.io/en/latest/reference/services/s3.html) ranges from very thorough to fairly lazy.

```python
import boto3

session = boto3.Session(profile_name='awsday-admin')
s3 = session.client('s3')
```

You may not need to use a [boto3.Session](http://boto3.readthedocs.io/en/latest/guide/session.html?highlight=session) object.
Sessions store credentials, region selection, etc.
Without a Session, you'll automatically get the creds from your "default" profile.

A `boto3.client('s3')` or `session.client('s3')` Client object is a low-level interface to the AWS service you specify.
A Resource, acquired as `boto3.resource('s3')` or `session.resource('s3')` also contains a Client, but it's a higher-level interface that can sometimes make your code easier to write.

The only [S3.Client](http://boto3.readthedocs.io/en/latest/reference/services/s3.html#client) method you'll need here is [s3.upload_file()](http://boto3.readthedocs.io/en/latest/reference/services/s3.html#S3.Client.upload_file).
Take a look at its documentation (linked in the previous sentence).

Example usage: `s3.upload_file('css/style.scss', 'zerotoboto', 'assets/css/style.scss')`.
This differs from the official documentation by not needing the `s3.meta.client` portion because our "s3" object above *is* a client, not a resource.

Over time you'll learn more of the style and particular methods and objects involved with using boto.
Later, you'll also want to `import botocore` so you can catch exceptions thrown by the boto3 module.
But don't worry about that for this script.

See also:
- [Boto3 S3 examples](http://boto3.readthedocs.io/en/latest/reference/services/s3.html#examples)
- [SQS tutorial](http://boto3.readthedocs.io/en/latest/guide/sqs.html)


---

## Exercise: Uploading files to S3

```
chris@CSU:~/work/ZeroToBoto/assets$ python backup-complete.py 
Uploaded /home/chris/work/ZeroToBoto/assets/rpg-3.py
      to zerotoboto:assets/rpg-3.py
Uploaded /home/chris/work/ZeroToBoto/assets/hangman-0.py
      to zerotoboto:assets/hangman-0.py
Uploaded /home/chris/work/ZeroToBoto/assets/css/style.scss
      to zerotoboto:assets/css/style.scss
```


## Hints

1. The boto3 docs give a handful of examples of the parts that you'll need for this.
2. Feel free to refer to the completed example for boto3 usage if you want to.
	Especially when learning a module that isn't part of a long-standing standard, the more working example code you can look at, the better.

[The completed backup script.]({{ site.baseurl }}/assets/backup-complete.py)

---

## Extra credit

1. Don't upload anything in hidden directories.
	That includes things in non-hidden directories in hidden directories.
	`assets/.hidden-stuff/foo/bar.txt` shouldn't get uploaded.
2. Check the modified time of the object in S3, and don't upload if the local file isn't newer.
	This makes it faster to use the script again and again in one directory.
	See the [S3.ObjectSummary](http://boto3.readthedocs.io/en/latest/reference/services/s3.html#objectsummary) class' documentation.
3. Add another script that is a "download" or "recover" version.
	List all objects in the bucket in a prefix that matches the current working directory's name (not the full path; just the lowest folder name).
	[<tt>s3.list_objects_v2()</tt>](http://boto3.readthedocs.io/en/latest/reference/services/s3.html#S3.Client.list_objects_v2) will be needed.
	Download every object found in S3, also creating directories on the local disk as needed (if S3 doesn't do it for you, use [<tt>os.mkdir()</tt>](https://docs.python.org/2/library/os.html?highlight=os%20mkdir#os.mkdir)).
4. Make a modified version of the script that doesn't just upload, but "synchronizes" the files it finds.
	If the modified time of the file is newer in S3 than it is locally, downlad the file instead of uploading it.
	Checking the hash to avoid unnecessary downloads (bandwidth out of AWS is billed) would be good, but isn't as straight-forward as you'd expect.

