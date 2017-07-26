---
category: info
info_order: 5
date: 2017-07-25 00:25 -07:00
title: Adventure game
---

```bash
You enter the Cave Entrance.
You see: Curved walls leading into darkness.
Paths: ['forward', 'trapdoor']
Choose your path: forward
You enter the Hallway.
You see: A long way forward with another path to the left.
Paths: ['pressure-plate', 'back', 'left']
Choose your path: 
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
chris@CSU:~/work/ZeroToBoto$ python assets/rpg-0.py 
Hiro (20/20 hp)
Slime A (5/5 hp)
```

Example of using your new class in the interpreter:

```python
>>> player = Character('Hiro', 20)
>>> print str(player)
Hiro (20/20 hp)
```

Create a <tt>Character</tt> class that has a name, current HP, and max HP, all tracked per instance of that class.
Give that class the special function `__str__(self)`.
`__str__` is what Python calls on an object when you ask to convert it to a string, such as for printing.
This is a very useful method to add to your classes.

Create a couple of character objects, and print each of them out in a human-friendly way (like above).

[The completed example.]({{ site.baseurl }}{% link /assets/rpg-0.py %})

