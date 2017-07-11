---
category: info
info_order: 3
date: 2017-06-17 21:50 -07:00
title: Guessing game
---

```
Guess my number (1-100): 42
Too low!
Guess my number (1-100): _
```

<!-- more -->

```python
$ python
>>> foo = 5
>>> print foo
5
>>> foo * 5
25
>>> foo = 10
>>> foo
10
```

By writing something like `foo = 5`, you're declaring that a variable named ("identified by") `foo` exists, and its value is 5.
You can perform various operations on foo, and it will retain whatever new value is assigned into it.

Python follows a common theme in most programming languages with the meaning of `=`.  This isn't the mathematical statement of "left and right are equal", but the *assignment operator*.
It means "take the thing on the right, and store it in the variable on the left".

To ask the question "are these two things equal", you write `foo == bar`.  Or to negate it, "are these two things *not* equal", you can do `foo != bar`.

Anytime you have a question on how something works in Python, asking or looking up documentation is good, but the interpreter is the ultimate source of truth as to what will happen.

```python
>>> a = 5
>>> b = a
>>> b
5
>>> b == a
True
>>> a = 10
>>> b
5
>>> b == a
False
```

For the more built-in types like numbers and strings, b will actually or effectively get a copy of what was assigned into a.

---

## Getting user input

```python
>>> raw_input()
I typed this in
'I typed this in'
>>> a = raw_input()
5
>>> b = 5
>>> a == b
False
>>> b = '5'
>>> a == b
True
```

There's a built-in function, <tt>[raw_input([prompt])](https://docs.python.org/2/library/functions.html#raw_input)</tt>, which lets your program take input from a user.
`raw_input` returns, *as a string*, whatever the user typed in.  Even if they typed in a number.
You can see this yourself when `a`, the user's input (above) is tested for equality against `b`, which is the integer 5.  It's `False`.  But if `a` is compared to the *string* `'5'`, then it's `True`.

---

## Exercise: The least dynamic guessing game in the world

Using what you know, make a .py file with a hard-coded "random" number for the computer, that a human has to guess by typing in some value.

Interacting with it should look like this:
```bash
chris@CSU:~/work/ZeroToBoto$ python assets/guessing-game-0.py 
Guess my number (1-5): 3
False
chris@CSU:~/work/ZeroToBoto$ python assets/guessing-game-0.py 
Guess my number (1-5): 4
True
```

### Hints
<ol>
<li>You can do this in three or fewer lines of Python.  Don't overthink it!</li>
<li>Comments in Python <code># are anything following a hash/sha/pound symbol.</code></li>
<li>
	<div> <!-- just to make Jekyll keep the spoiler stuff together -->
	<a href="#spoiler-open-0-1" id="spoiler-open-0-1" class="trigger open">How to get the "Guess my number" prompt...</a>
	<a href="#spoiler-close-0-1" id="spoiler-close-0-1" class="trigger close">How to get the "Guess my number" prompt...</a>
	<div class="spoiler">
	<code>raw_input</code>, described above with a link to its documentation, can take an optional "prompt" parameter.
	</div>
	</div>
</li>
<li>
	<div>
	<a href="#spoiler-open-0-2" id="spoiler-open-0-2" class="trigger open"><code>str</code> vs. <code>int</code>...</a>
	<a href="#spoiler-close-0-2" id="spoiler-close-0-2" class="trigger close"><code>str</code> vs. <code>int</code>...</a>
	<div class="spoiler">
	Store the computer's number as <code>'3'</code>, not <code>3</code>.  You want a <code>str</code> (String) to compare it to the user's input from <code>raw_input</code>, which is always a <code>str</code>.  Without the quotes, Python takes it to be an <code>int</code>.
	</div></div>
</li>
<li>
	
	<div>
	<a href="#spoiler-open-0-3" id="spoiler-open-0-3" class="trigger open">How to use the user's input later...</a>
	<a href="#spoiler-close-0-3" id="spoiler-close-0-3" class="trigger close">How to use the user's input later...</a>
	<div class="spoiler">
	Store the result of <code>raw_input</code> in a variable.  <code>guess = raw_input()</code>.
	</div></div>
</li>
<li>
	<div>
	<a href="#spoiler-open-0-4" id="spoiler-open-0-4" class="trigger open"><code>True</code> and <code>False</code> aren't printing...</a>
	<a href="#spoiler-close-0-4" id="spoiler-close-0-4" class="trigger close"><code>True</code> and <code>False</code> aren't printing...</a>
	<div class="spoiler">
	When you're using the interpreter interactively, the result of a statement like <code>2 + 2</code> (<em>not</em> <code>a = 2 + 2</code>) is treated in a special way.  Since a result isn't being stored anywhere, the interpreter prints it out for you to see on the next line.  That's why <code>5 == '5'</code> prints <code>False</code> when working interactively, but the same line in a .py script doesn't print anything out.  In that case, just <code>print 5 == '5'</code> instead.
	</div></div>
</li>
</ol>

[A completed example.]({{ site.baseurl }}/assets/guessing-game-0.py)

---

## Flow control

### If, else

```python
if 1 > 2:
    print "Everything's broken."
else:
    print "All's well."
```

When the statement between the `if` keyword and `:` is "true", the indented lines of code after the `if` are executed.
If that statement isn't true (technically `False` or `None`), the `if` statement's indented lines are *not* run.
If there's an `else` right after it (you don't have to have one), then the `else`'s indentend block of statements is executed instead.

Remember that Python cares about indenting!

```python
if False:
    print "This will never print."
    print "Neither will this; still the same 'if' block."
print "But this will."

if False:
    print "This won't print."
    else:  # Invalid.  This 'else' doesn't line up with any 'if'.
        print "Neither will this; Python dissapproves of your bad whitespace."
```

### While

```python
user_input = 'y'
# Here's a new operator.  '==' is "equal-to", '!=' is "not-equal-to".
while user_input != 'n':
    user_input = raw_input("Continue? [y/n]: ")
print "Done."
```

```bash
$ python while-example.py
Continue? [y/n]: y
Continue? [y/n]: banana
Continue? [y/n]: no
Continue? [y/n]: n
Done.
$ _
```

`while` is a lot like `if`, but it has this looping behavior added:
<!-- credit to http://asciiflow.com/ for the nice ASCII flowchart tool -->
<pre>
+--------------------------------+
|                                |
| Is the 'while' statement true? <-------+
|                                |       |
+---------+---------+------------+       |
          |         |                    |
          No       Yes                   |
          |         |                   Loop
          |         |                    |
          |         |         +----------+-----------------+
          |         |         |                            |
          |         +---------> Run statement(s) in block. |
          |                   |                            |
          |                   +----------------------------+
          |
          |
+---------v---------------------------+
|                                     |
| Skip statement block.               |
| Continue at next non-indented line. |
|                                     |
+-------------------------------------+
</pre>

---

## Exercise: Guessing repeatedly

Update the previous exercise to make the user guess until they're right.
Comparing the example of how it should look below to the previous one: a wrong guess doesn't end the program, and just prompts again immediately.

Alternately, you could make it print "True" or "False" after every guess.  Either is equally correct for this exercise.

```bash
chris@CSU:~/work/ZeroToBoto$ python assets/guessing-game-0.py 
Guess my number (1-5): 3
Guess my number (1-5): 4
True
```

### Hints

<ol>
<li>
	<div>
	<a href="#spoiler-open-1-1" id="spoiler-open-1-1" class="trigger open">Flow control...</a>
	<a href="#spoiler-close-1-1" id="spoiler-close-1-1" class="trigger close">Flow control...</a>
	<div class="spoiler">
	Use a <code>while</code> whose test involves the user's input.
	</div>
	</div>
</li>
<li>
	<div>
	<a href="#spoiler-open-1-2" id="spoiler-open-1-2" class="trigger open"><code>NameError: name 'user_guess' is not defined</code>...</a>
	<a href="#spoiler-close-1-2" id="spoiler-close-1-2" class="trigger close"><code>NameError: name 'user_guess' is not defined</code>...</a>
	<div class="spoiler">
	Before you can test a variable for anything, it needs some value stored in it so it exists (is defined).  Before your <code>while</code> test, assign any-old not-correct thing to the variable.  <code>user_guess = "can't be a right answer"</code>.
	</div>
	</div>
</li>
<li>You <em>might</em> be able to complete this by adding two lines, and indenting one other.</li>
</ol>

[A completed example.]({{ site.baseurl }}/assets/guessing-game-1.py)

---

<h2>Variable types, <tt>str</tt> vs. <tt>int</tt></h2>

Why is `32 == '32'` `False`?  32, as an `int`, is represented as an integral number that the CPU can deal with very quickly.
It has hardware dedicated to performing very basic math operations on it.
Here's what it actually looks like: <code>0000 0000 &nbsp;0000 0000 &nbsp;0000 0000 &nbsp;0000 0000 &nbsp;0000 0000 &nbsp;0000 0000 &nbsp;0000 0000 &nbsp;0010 0000</code>.
Don't worry if you're not familiar with binary, it's not necessary to know it just here and now.
`int`s in 64-bit Python 2 are 8 bytes (hence the 8 * 8 (or 64) zeroes-and-ones above).

While `'32'`, the string, is text encoded in ASCII.  Not a number.
Each character in a string is one byte.  `'32'` looks like this: <code>0011 0011 &nbsp;0011 0010</code>.
Neither byte is the number 3, 2, or 30 on their own.
They're each 50 and 51, the ASCII encodings of `'3'` and `'2'`.

So strings are text that can be of just about any length, and contain just about any character.
Integers (in 64-bit Python 2) are limited to the range -9,223,372,036,854,775,806 to +9,223,372,036,854,775,807.

Summary: `int` is a computer-friendly "natural" (no fractions) number.  `str` is text, on which you can't perform math.
(Also if you do want fractions, that's a `float`.  We'll look at that another time.)

Python provides an easy way to *cast* values between the different types in a human-friendly way.
You basically call a function that is the desired type's name, and pass it the thing you want cast into that type.

```python
>>> '32' == 32
False
>>> '32' == str(32)
True
>>> int('32') == 32
True
>>> int('3.14')  # Not something an int can represent!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: '3.14'
```

If you compare two strings, they'll order lexicographically (this is not true of all programming languages!).
Note that uppercase letters come before lower-case letters, because their underlying value in ASCII encodings is lower.
Here's an [ASCII table](https://duckduckgo.com/?q=ascii+table&iar=images&iax=1&ia=images&iai=https%3A%2F%2Fs-media-cache-ak0.pinimg.com%2F736x%2F95%2Fdd%2Fc8%2F95ddc8a6c29eb2187336c8b5efd31c28.jpg) that shows these values.
This is why you commonly see URLs with "%20" where spaces might normally be expected.  20 is hex for decimal 32, which is space's value in ASCII.

```python
>>> 'a' < 'b'
True
>>> 'a' < 'B'
False
```

Be careful about mixing strings and ints.  You can get some very weird-looking results.

```python
>>> '500' < 2
False
>>> 500 < '2'
True
>>> '2' > 500
True
```

In short: *any* variable of a numeric type will *always* be "less than" any variable of the `str` type.
See [this Stack Overflow question](https://stackoverflow.com/questions/3270680/how-does-python-compare-string-and-int) for more, if you're interested.

---

## Exercise: Giving hints

Update the previous exercise to now give hints of "Too low" or "Too high" when the user misses the computer's number.

```bash
chris@CSU:~/work/ZeroToBoto$ python assets/guessing-game-2.py 
Guess my number (1-5): 3
Too low.
Guess my number (1-5): 5
Too high.
Guess my number (1-5): 4
Correct!  My number was 4
```

### Hints

<ol>
<li>You can't do math on strings.  Including less-than/greater-than comparison.</li>
<li>Don't worry about validating the user's input yet.  That's a topic for another day.  If they decide to type "wrench" for their guess and get a <a href="https://docs.python.org/2/library/exceptions.html#exceptions.ValueError"><tt>ValueError</tt></a> from Python, that's their problem.</li>
<li>Storing the computer's number as an <tt>int</tt> instead of a <tt>str</tt> will reduce the amount of casting you have to do.</li>
<li>If you get really stuck and <em>have</em> to look at the completed example below, try also diff'ing it against the previous completed example to see exactly what changed.</li>
</ol>

[A completed example.]({{ site.baseurl }}/assets/guessing-game-2.py)

---

## Importing more functionality

In Python you can <a href="https://docs.python.org/2/tutorial/modules.html"><tt>import</tt></a> other code to make it available to your program.
You can then call its provided methods as `module_name.function_name()`.

```python
>>> import random
>>> random.seed()  # prepare the random number generator
>>> random.randint(1, 5)
1
>>> random.randint(1, 5)
4
```

Python is well known for its vast ecosystem of modules.
It has many great built-in modules ([re](https://docs.python.org/2/library/re.html), for regular expressions, is a favorite), and many more can be installed as easily as `pip install <module-name>`.

Modules, in their most basic form, are just other .py files.
We'll make our own later so future scripts can import our old functionality.
As you use Python over time, you'll slowly build up a library of re-usable code from your past work.
This makes future work that much faster, as you won't have to redo past solutions.

---

## Exercise: Completed guessing game

Update the previous exercise to have a larger range (1-100), and for the computer to finally have an interesting (random) number, instead of a hard-coded value.

```bash
chris@CSU:~/work/ZeroToBoto$ python assets/guessing-game-complete.py 
Guess my number (1-100): 42
Too low.
Guess my number (1-100): 90
Too low.
Guess my number (1-100): 95
Too low.
Guess my number (1-100): 98
Too high.
Guess my number (1-100): 96
Correct!  My number was 96
```

### Hints

1. See the documentation on [<tt>randint()</tt>](https://docs.python.org/2/library/random.html#random.randint).

[The complete guessing game.]({{ site.baseurl }}/assets/guessing-game-complete.py)

---

## Extra credit

1. Have the game print how many guesses were made after it's over.
2. Have the user type in an upper-bound for the random range.
	- Update the "Guess my number" prompt to match.  Refer back to [Hello, Python!]({{ site.baseurl }}/hello-python) for string concatenation help.  Remember to cast.
3. Instead of quitting when correct, ask if the user wants to play again.<br/>
	Hint: Defining more functions is recommended.

