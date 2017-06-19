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

<script lang="css">
.spoiler {
	    display: none;
}

.trigger.close {
	    display: none;
}

.trigger.open:target {
	    display: none;
}

.trigger.open:target + .trigger.close {
	    display: inline;
}
</script>

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
	`raw_input`, described above with a link to its documentation, can take an optional "prompt" parameter.
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

### If

### While

---

## Exercise: Giving hints

Too low, too high...

---

## Exercise: Guessing repeatedly

---

## Importing more functionality

### The random module

---

## Exercise: Complete guessing game

---

[The complete guessing game.]({{ site.baseurl }}/assets/guessing-game-complete.py)

