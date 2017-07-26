---
category: info
info_order: 5
date: 2017-07-25 00:25 -07:00
title: Adventure game
---

```bash
You enter the Cave Entrance.
You've been here 1 time(s).
You see: Curved walls leading into darkness.
Paths: ['forward', 'trapdoor']
Choose your path: forward
 
You enter the Hallway.
You've been here 1 time(s).
You see: A long way forward with another path to the left.
Paths: ['pressure-plate', 'back', 'left']
Choose your path: _
```

<!-- more -->

## Classes

Classes are very useful for having a collection of stuff that agrees to some way of interacting with it, and writing very simple code that uses that means of interacting, without necessarily knowing what it's using.
You describe the behavior of something in a class, then re-use that behavior throughout your code by creating "instances of" that class.
Instances of a class are also called "objects" of a class; you'll see both terms used interchangeably.

A good analogy for classes versus objects is that a class is a blueprint for how to build a house.
An object is a house made from that blueprint.
The blueprint defines how things work and fit together, but you can't live in a blueprint or fill it with actual things.
You can have many houses made from the same blueprint.
They'll all work the same way, but painting one house red doesn't suddenly paint every house made from that blueprint red as well.

For example, let's say Clothing is a class.
If I tell you I have an object of clothing, you already know some basic things about how it's used and what it does, without me saying anything more.
Further, you may have an object of Clothing that's red, and I have an object of Clothing that's blue.
Nothing about their use or behavior changes (they're both objects of Clothing), but data associated with each individual *instance* of Clothing changes.

Some basic code can operate on a list of *things*, and let them drive what that actually means.
This lets you easily extend some functionality you have later on by just creating one new class.
*Without* needing to touch the code you've already debugged and figured out is just right for the basic intent of the program.

Back at the Clothing example, you may have some objects of Clothing and some of Cookware.
These are different types, but you can load some number of objects of either type into a box and donate it all to a charity.
Your generic "get box of stuff to charity" procedure doesn't change due to the objects' types changing, so it can operate the same way no matter what you add to the box.
While the charity on the receiving end will invoke different behavior depending on what types it receives.
Generally, this is how you want to structure your code involving classes and objects.
Try to keep as much of your program's overall behavior as indifferent as possible to the inner-workings of objects as you can.

```python
class Dog(object):  # defining a new class/type
    def speak(self):  # defining a function within that class
        print 'woof'  # function's implementation

class Cat(object):
    def speak(self):
        print 'meow'
```

```python
>>> fido = Dog()
>>> fido.speak()
woof
>>> animals = [fido, Dog(), Cat()]
>>> for animal in animals:
...        animal.speak()
...
woof
woof
meow
```

When you want to use a class, you create a new a new *object* of that class' *type* by giving the class name followed by parentheses.
It's like there's a function that is the class' name, which gives you back a new object its type.

To call a class' function, it's `object_name.function_name()`.
Similar to using a function defined within a module (`random.randint()`).
Only here, the object you're calling any functions with actually gets passed as the first parameter to that function.
This first parameter is traditionally named "self", and you should absolutely follow that practice.

> If you're coming from other languages where this example requires a common base class <tt>Animal</tt> between these two types, this is a bit different in Python.
> Python is strongly typed (Dog is not Cat), but you can also mix and match types about as much as you want.
> So long as a type walks like a duck and sounds like a duck, to Python, it may as well be.
> ... Unless you specifically ask something like `isinstance(fido, Duck)`.

<!--
[New-style class documentation.](https://www.python.org/download/releases/2.2.3/descrintro/)
-->

---

## <tt>self</tt>

The above are classic examples in programming of how to use classes, but not good ones to follow design-wise.
Classes should be created when it helps to reduce duplicating *functionality*.
They're similar to functions in this way, but classes make it easier to bundle functionality together and aid readability.
Since the functionality is the same between Dog and Cat (call "speak" and have something get printed out), there should be only one class here.
The message that's "spoken" is just data that should be on an object.
To do which, you need to use <tt>self</tt>.

`self` is always the object you're calling the class' function with.
We didn't use `self` in the above Dog/Cat examples; the function "speak" just printed out a message no matter which instance it was called on (it differed by class, not object).

```python
class Animal(object):
    def __init__(self, sound):
        # copy the passed-in value to this object's data
        # (the names don't have to match)
        self.sound = sound

    def speak(self):
        print self.sound
```

```python
>>> fido = Animal('woof')
>>> fido.speak()
woof
>>> animals = [fido, Animal('woof'), Animal('meow')]
>>> for animal in animals:
...        animal.speak()
...
woof
woof
meow
```

`__init__` is a special function.
Whenever an object is being instantiated (first created and initialized), its type's `__init__` function is called; again passing the object as the first parameter, "self".
This lets you setup objects of your type with some default values and variables assigned.
It's very often a good idea to give your types an `__init__` function.

You can also define your `__init__` with more parameters than just <tt>self</tt>, and then you can take in more parameters during object creation.
Note `Animal('woof')` *looks* like you're just giving it one parameter, while the function expects two (<tt>self</tt> and <tt>sound</tt>).
But, because of that special <tt>self</tt> behavior on functions defined in a class, it's actually getting the object being instantiated/initialized, *then* whatever arguments you called the function with.

In Python, assigning to a variable makes it exist.
So assigning to `self.sound` in the Animal `__init__` function makes whatever object "self" happens to be gain a variable named "sound", and gives it some value.
Don't forget to use `self.` in your <tt>\_\_init\_\_</tt> functions!
If you just write `sound = sound` instead, your object won't store anything.
That's just a function-local `sound` that'll get thrown away when we leave the function.

All this special <tt>self</tt> behavior really boils down to is "syntactic sugar".
A language feature that saves you some typing.
Writing `fido.speak()` is "exactly" the same as `Dog.speak(fido)`.
It's just a function that exists within some scope (the Dog class; as opposed to a module or other), and it takes one parameter.
Its one parameter is *expected* to be an object of the Dog class.

```python
>>> fido.speak()
woof
>>> Animal.speak(fido)
woof
```

---

## Exercise: Create a class

```bash
chris@CSU:~/work/ZeroToBoto$ python assets/adventure-0.py 
You see: An indescribable room.
You see: Curved walls leading into darkness.
```

Example of using your new class in the interpreter:

```python
>>> entry = Room('Cave Entrance')
>>> entry.description = 'Curved walls leading into darkness.'
>>> entry.describe()
You see: Curved walls leading into darkness.
```

Create a <tt>Room</tt> class that has a name and a description.
You should be able to initialize Room objects with their name (as shown above), and set their description (also seen above).
Add a <tt>describe</tt> function that mimics what's been demonstrated above.

Create a couple of room objects, and have them <tt>describe</tt> themselves.

### Hints

<ol>
{% include spoiler-hint.html major=0 minor=1
	summary="<tt>describe</tt> oneself"
	details="
		Remember the <tt>describe</tt> function will need to take one parameter: <code>self</code>
" %}
{% include spoiler-hint.html major=0 minor=2
    summary="Object initialization"
    details="It's almost always a good idea to have an <code>__init__(self)</code> function that assigns <em>something</em> to each variable name you want an object of a given class to hold.
" %}
</ol>

[The completed example.]({{ site.baseurl }}{% link /assets/adventure-0.py %})

---

## Dictionaries

```python
>>> stats = {}
>>> stats['hp'] = 14
>>> stats['dexterity'] = 7
>>> print stats
{'dexterity': 7, 'hp': 14}
```

```python
>>> class Turtle(object):
...     def __init__(self, color):
...         self.color = color
...
>>> turtles = {'leonardo': Turtle('blue'), 'donatello': Turtle('purple')}
>>> turtles['michaelangelo'] = Turtle('orange')
>>> turtles['raphael'] = Turtle('red')
>>> print turtles['donatello'].color
purple
```

Dictionaries are collections of things, somewhat like lists, but you give each item in a dictionary a unique name.
More generically, its name is its "key", which can be of nearly any type.
Items (more generically, "values") are easy to access at random by *indexing* the dictionary with a value's key.
However, dictionaries don't have a specific human-ey order to them like lists.
So if you're enumerating items in a dictionary without using their keys, rely on not getting them in a predictable order.

Dictionaries use curly braces `{}`, as opposed to lists' square brackets `[]`.
You can create them empty (like "stats" above), or with some items already in them (like "turtles" above).
If defining key-value pairs when you declare the dictionary, the format is `key: value,key2: value2`, and so on.
To add key-value pairs into a dictionary (officially the `dict` type) later on, index the dictionary with the desired key, and assign to it the desired value.

Check out the [<tt>dict</tt> documentation](https://docs.python.org/2.7/library/stdtypes.html?highlight=dict#dict) for information on helpful things like the [<tt>.keys()</tt>](https://docs.python.org/2.7/library/stdtypes.html?highlight=dict#dict.keys) function.

---

## Exercise: Making connections

```bash
chris@CSU:~/work/ZeroToBoto$ python assets/adventure-1.py 
You see: Curved walls leading into darkness.
Paths: ['forward', 'trapdoor']
You see: An indescribable room.
Paths: []
You see: A long way forward with another path to the left.
Paths: ['right', 'back', 'left']
```

Example of use in the interpreter:

```python
>>> entry.describe()
>>> entry.connections['trapdoor'].describe()
>>> entry.connections['forward'].describe()
```

Give each room a dictionary of connections to other rooms.
The player will be presented with a list of connections available from the current room.
In the final game, they'll then type in the name of a connection, and move into the room it refers to.

[The completed example.]({{ site.baseurl }}{% link /assets/adventure-1.py %})

---

## Exercise: Make it interactive

```bash
chris@CSU:~/work/ZeroToBoto$ python assets/adventure-complete.py 
You enter the Cave Entrance.
You've been here 1 time(s).
You see: Curved walls leading into darkness.
Paths: ['forward', 'trapdoor']
Choose your path: forward
 
You enter the Hallway.
You've been here 1 time(s).
You see: A long way forward with another path to the left.
Paths: ['pressure-plate', 'back', 'left']
Choose your path: back
 
You enter the Cave Entrance.
You've been here 2 time(s).
You see: Curved walls leading into darkness.
Paths: ['forward', 'trapdoor']
Choose your path:
```

Add a 'visit' counter to each room, adding to it each time the player enters a room.
You'll need to have at least one way to get back to an earlier room to demonstrate that this works.
This is mostly just to be sure you know how to refer to the object you mean to, without being able to cheat and hardcode the object's name in.

Have the player pick from a set of available connections out of their current room into others.
Do this again and again until the player types "quit" or enters a room with no connections leading out of it.

Make at least four rooms.
An entry, a 'good ending' room, a 'bad ending' room, and one other.
You should have at least one room with no connections, at least one with one connection, and at least one with two or more connections.
Each room should have its own unique set of connections.

### Extra credit

- Make a room that can be "modified".
    Emphasis on the double-quotes there.
    Play the completed game example to see what I mean.
- Give rooms some set of items (make a new Item class).
    These items can be taken by the player by typing their name in instead of a connection's name.
    Score the player's result at the end of the game based on the sum value of all items collected.
- Instead of navigating rooms, make a conversation with an NPC.
    The NPC should be able to "recall" past selections from the player and react differently to the same input based on that.

[The complete adventure game.]({{ site.baseurl }}{% link /assets/adventure-complete.py %})

