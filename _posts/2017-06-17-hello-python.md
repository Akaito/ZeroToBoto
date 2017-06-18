---
category: info
info_order: 2
date: 2017-06-17 17:08 -07:00
title: Hello, Python!
---

```python
$ python
>>> 2 + 2
4
>>> print "Hello, Python!"
Hello, Python!
>>> exit()
```

<!-- more -->

By entering just `python` on the command line, you're put into the [Python interpreter](https://docs.python.org/2/tutorial/interpreter.html).
Anything you type into the interpreter (followed by pressing &lt;Enter&gt;) is a single line of Python script/code, which is immediately run.
The next line prints some representation of the result of your statement, if there's anything meaningful to show.  The interpreter is very useful for quickly testing if something works the way you think it should in Python.

`2 + 2` results in `4` being printed, because your statement was interpreted something like `<number> <operator> <number>`, the operation was performed,
and the final result was rendered as some text output.

`exit()` is saying "call the `exit` function", whose job it is to quit the interpreter/script, which gets us back to a normal command line.
To the interpreter, this ends up looking like `call <function> no-arguments`.  Anytime you have `sometext` followed by an opening parenthesis `(`,
you're saying "call the function named `sometext`".

A function is any re-usable chunk of code, usually with a name to make it easy to call.  Functions can take zero or more arguments, and can return
zero or more results.  Multiple results is not a common feature of many languages.  `exit` can take zero arguments, and it returns zero results.

`print` is also a function like `exit`.  Pre-Python 3 it cheats by being a special case that doesn't need parentheses to be called, for historical reasons.
`"Hello, Python!"` is the single argument we passed to the <tt>[print](https://docs.python.org/2/library/functions.html?highlight=print#print)</tt> function.  All `print` does is take all arguments it's given, render
them as text, and spit them back out at us.  Since we gave a [string](https://docs.python.org/2/library/string.html) (anything between
two double-quotes, or two single-quotes), rendering that as text is completely straight-forward (it already *is* text).
So the interpreter saw something like `call <function> one-argument <string>`.  Fairly similar to `exit()` above, but this time with one argument.

In fact, even the simple addition we did above is ultimately a function call with two arguments and one result.
Being able to write it out as `2 + 2` instead of `add(2, 2)` is just a nicety that most languages support.
Ultimately, the interpreter treats that as something like `call <function> two-arguments <number> <number> expect-one-result`.

---

## Defining our own functions

```python
$ python
>>> def say_hello():
...     print "hello"
... 
>>> say_hello()
hello
```

You define functions by saying `def <function-name>():` in the first line.
After that, you can see the Python interpreter telling us something new.  Instead of each line after we press &lt;Enter&gt; starting out with `>>>` ("waiting for input"), there's now `...`, which means "waiting for *continued* input".
We haven't finished our statement yet (for the function's definition).

Whitespace/indentation **is important** in Python.  Each statement within your function must be indented.  Python doesn't care if you use a tab, two spaces, or four spaces, so long as you're *consistent* about it.
Now that you're indented on this line, just call `print` like you did before.  Then press &lt;Enter&gt; to complete that line, and &lt;Enter&gt; once more on a blank line to complete the function definition.

Once you're back at `>>>`, your function definition statement is complete.  Until you `exit()`), you can call your new function as `say_hello()` over and over.

```python
$ python
>>> def write_test(address):
...     print "ping -n 5 -a " + address
...     print "tracert " + address + " > trace-result." + address + ".txt"
... 
>>> write_test("10.0.20.5")
ping -n 5 -a 10.0.20.5
tracert 10.0.20.5 > trace-result.10.0.20.5.txt
>>> write_test("10.0.21.42")
ping -n 5 -a 10.0.21.42
tracert 10.0.21.42 > trace-result.10.0.21.42.txt
```

`write_test` takes one argument (named "address"), prints some stuff out, and returns nothing.
Printing *is not* returning something.  Printing writes to the "stdout" (standard out) stream.
This is the same way of communicating with the terminal as you're used to from most programs.  Once we're using saved scripts instead of the interpreter, anything printed with `print` can be redirected to a text file with `foo > result.txt` like you're used to.

`print "ping -n 5 -a " + address`<br/>
`address` is the name of `write_test`'s one argument.  Here we're assuming it's a string and it can just be added to (appended to) another string.  If someone mis-uses your function and gives a non-string (something note quoted), you'll get an error.

```python
>>> write_test(10)
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in write_test
TypeError: cannot concatenate 'str' and 'int' objects
```

`int` is the type of any "natural" number (0, 1, 2, -4, 5000).<br/>
`float` is the type of any "fractional" number (1.0, 3.14, 0.5).<br/>
In neither case does it make sense to Python to append a number to a string.

You may have encountered this, if you forgot to quote your input:
```python
>>> write_test(10.0.20.5)
  File "<stdin>", line 1
    write_test(10.0.20.5)
                     ^
SyntaxError: invalid syntax
```

Python saw a non-quoted digit, assumed we were giving it a number, saw the first period, considered it to be a `float`, then got confused when a second period showed up.

---

## Saving work for later

Using your favorite text editor, copy in the *input* from our last example:
```python
def write_test(address):
    print "ping -n 5 -a " + address
    print "tracert " + address + " > trace-result." + address + ".txt"

write_test("10.0.20.5")
write_test("10.0.21.42")
```

Save that as write-test.py, or any other helpful name ending in ".py".  Now run `python write-test.py` from the directory where you saved that file.
This is somewhat like telling the Python interpreter to take each line of the file and run it as if you typed it in.  Only now you can just do it again later without typing it all out again.

To make this a more useful tool in the future, delete the two calls to `write_test` at the end, so the file only has your function definition.
Now instead run `python -i write-test.py`.  Just like before, your script will be run by the interpreter.  But now you're placed in "inspect"/"interactive" mode right after it finishes, with everything from the script still in existence.  Trying entering `write_test("foo")` now, and you'll see your function run.

```python
$ python -i write-test.py
>>> write_test("10.0.20.5")
ping -n 5 -a 10.0.20.5
tracert 10.0.20.5 > trace-result.10.0.20.5.txt
```

Now just copy-paste that printed output either into a .bat file, or straight onto a command line.

