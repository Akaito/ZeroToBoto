---
category: info
info_order: 2
date: 2017-06-17 17:08 -07:00
title: Hello, Python!
---

<pre>
$ python
>>> 2 + 2
4
>>> print "Hello, Python!"
Hello, Python!
>>> exit()
</pre>

<!-- more -->

By entering just `python` on the command line, you're put into the [Python interpreter](https://docs.python.org/2/tutorial/interpreter.html).
Anything you type into the interpreter (followed by pressing &lt;Enter&gt;) is a single line of Python script/code, which is immediately run.
The next line prints some representation of the result of your statement, if there's anything meaningful to show.

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

<pre>
$ python
>>> def say_hello():
...     print "hello"
... 
>>> say_hello()
hello
</pre>

You define functions by saying `def <function-name>():` in the first line.
After that, you can see the Python interpreter telling us something new.  Instead of each line after we press &lt;Enter&gt; starting out with `>>>` ("waiting for input"), there's now `...`, which means "waiting for *continued* input".
We haven't finished our statement yet (for the function's definition).

Whitespace/indentation **is important** in Python.  So the first thing you want to do after naming your function and getting the `...` input continuation, is to hit tab.  Python doesn't care if you use a tab, two spaces, or four spaces, so long as you're *consistent* about it.
Now that you're indented on this line, just call `print` like you did before.  Then press &lt;Enter&gt; to complete that line, and &lt;Enter&gt; once more on a blank line to complete the function definition.

Once you're back at `>>>`, your function has been defined.  Now and forever more (until you `exit()`), you can call your new function as `say_hello()`.
This becomes more useful with more complicated or repetitive functions, and those that take arguments.

<pre>
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
</pre>

`write_test` takes one argument, prints some stuff out, and returns nothing.

- [ ] Explain why `write_test` returns nothing, but we see output.  Maybe differentiate from `2 + 2` statement earlier.
- [ ] Add header that all posts use to "h1" their title.

