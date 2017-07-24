---
category: info
info_order: 5
date: 2017-07-12 00:25 -07:00
title: RPG combat
---

```bash
Your attacks:
  Slash (4 dmg)
  Heal (8 healing)
Remaining combatants:
  Hiro (20/20 hp)
  Slime A (5/5 hp)
  Slime B (5/5 hp)
<attack> <combatant>: slash slimea
Hiro used Slash (4 dmg) on Slime A (1/5 hp)
Slime B used Disintegrate (9 dmg) on Hiro (11/20 hp)
Slime B used Disintegrate (9 dmg) on Slime B (0/5 hp)
Slime A used Acid (2 dmg) on Hiro (9/20 hp)
Slime B has died!
```
<!-- more -->

## Classes

Classes are very useful for having a collection of stuff that agrees to some way of interacting with it, and writing very simple code that uses that means of interacting, without necessarily knowing what it's using.
You describe the behavior of something in a class, then re-use that behavior throughout your code by creating "instances of" that class.
Instances of a class are also called "objects" of a class; you'll see both terms used interchangeably.

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
Only here, the object you're calling any of its functions on actually gets passed as the first parameter to that function.
This first parameter is traditionally named "self", and you should absolutely follow that practice.

> If you're coming from other languages where this example requires a common base class <tt>Animal</tt> between these two types, this is a bit different in Python.
> Python is strongly typed (Dog is not Cat), but you can also mix and match types about as much as you want.
> So long as a type quacks like a duck and walks like a duck, to Python, it may as well be.
> ... Unless you specifically ask something like `isinstance(fido, Duck())`.

<!--
[New-style class documentation.](https://www.python.org/download/releases/2.2.3/descrintro/)
-->

---

## <tt>self</tt>

`self` is always the object you're calling the class' function with.
We didn't use `self` in these Dog/Cat examples; the function "speak" just prints a message no matter which instance it's called on.

```python
class RemoteMachine(object):
    def __init__(self, ip):
        self.ip = ip

    def ping(self):
        response_ms = some_imaginary_module.send_ping(self.ip)
        print response_ms
```

```bash
>>> machines = [
...     RemoteMachine('127.0.0.1'),
...     RemoteMachine('10.0.0.1')
... ]
>>> for machine in machines:
...        machine.ping()
...
0.09
2.2
```

`__init__` is a special function.
Whenever an object is being instantiated, its type's `__init__` function is called; again passing the object as the first parameter, "self".
This lets you setup objects of your type with some default values and variables assigned.
It's very often a good idea to give your types an `__init__` function.

You can also give `__init__` more parameters than just <tt>self</tt>, and then you can take in more parameters during object creation.
Note `RemoteMachine('10.0.0.1')` *looks* like you're just giving it one parameter, while the function expects two ("self" and "ip").
But, because of that special "self" behavior on class functions, you're actually giving it the object, *then* whatever extra arguments you filled in.

In Python, assigning to a variable makes it exist.
So assigning to `self.ip` in the RemoteMachine `__init__` function makes whatever object "self" happens to be have a variable named "ip", and gives it some value.
Don't forget to prefix your object variable access with `self.`!

All this special <tt>self</tt> behavior really boils down to syntactic sugar.
`fido.speak()` is exactly the same as `Dog.speak(fido)`.
It's just a function that exists within some scope (the Dog class; as opposed to a module or other), and it takes one parameter.
Its one parameter is *expected* to be an object of the Dog class.

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

---

## Inheritance

> It's good to have some familiarity with inheritance.
> Knowing it may sometimes make some of your scripts much easier to write.
> However, knowing how to use it isn't required to use AWS/boto.
> Normally more time is spent on introducing these topics.
> So don't become distraught if you don't get it all right away.
> This is a quick introduction to it to help you know how things work underneath.

`class Dog:` vs. `class Dog(object):`.
Classes can be defined in Python in either of these two ways.
The first is an old-style class; the second a new-style class.
Other than for specific compatibility issues with older code, you should make [new-style classes](https://docs.python.org/2.7/glossary.html#term-new-style-class) that inherit from <tt>object</tt>.
In the second way, you're saying that Dog "inherits from" or "is a subclass of" the <tt>object</tt> type.
`object` is the base-most type that most everything else inherits from.
If a type inherits from another type, the subclass also has all of the parent class' stuff.

```python
class GermanShepherd(Dog):
    pass  # nothing to do here; just let us complete the class definition
```

```python
>>> GermanShepherd().speak()
woof
```

The `pass` keyword is very useful for stubbing code in when you know something will eventually be there in the future.
It just means "I don't want to do anything here, but Python needs to see something indented here (not a comment) to make this valid.
So I explicitly <tt>pass</tt> on doing anything at this point."
It's not specifically related to inheritance in any kind of special way.

---

## Overriding behavior

```python
class Chihuahua(Dog):
    def speak(self):
        print 'yap'
```

```python
>>> Chihuahua().speak()
yap
>>> GermanShepherd().speak()
woof
```

Even though Chihuahua inherits from Dog, it gives a new definition to <tt>speak</tt>.
This new definition is only present in objects of type Chihuahua, and any other classes that inherit from Chihuahua.
Instances of Dog and GermanShepherd will still say 'woof'.

---

## Checking types

```python
>>> fido
<__main__.Dog object at 0x7fca85abc310>
>>> type(fido)
<class '__main__.Dog'>
>>> Dog
<class '__main__.Dog'>
>>> type(fido) == Dog
True
>>> type(Dog)
<type 'type'>
```

"\_\_main\_\_" is the special "module" name given to our script when its file is executed directly from Python or we're using the Python interpretor directly.
So in the above where you see `__main__.Dog`, that's of the format "&lt;module_name&gt;.&lt;type_name&gt;".
You can see that the `type()` of an object is exactly the class it was instantiated from.
The type of a class/type you've defined is, sensibly enough, `type`.
`type` is just a type of variable; much like `str` and `int`.

---

## Exercise: Adding abilities

```bash
chris@CSU:~/work/ZeroToBoto$ python assets/rpg-1.py 
Hiro (20/20 hp) has Slash (5 damage)
Slime A (5/5 hp) has Acid (2 damage)
```

Create a new <tt>Ability</tt> class that has a name and an integer amount of damage it deals.
Add an ability to the <tt>Character</tt> class, so each Character object knows what its Ability is.
Print out something like "&lt;character&gt; has &lt;ability&gt;" for each character, getting its ability from some variable stored on the individual Character object.
The printing can be done either in a class function or just out in the main script area.

[The completed example.]({{ site.baseurl }}{% link /assets/rpg-1.py %})

---

## Exercise: Performing abilities

```bash
chris@CSU:~/work/ZeroToBoto$ python assets/rpg-2.py 
Hiro (20/20 hp)
Slime A (5/5 hp)
 
Hiro used Slash (5 damage) on Slime A (0/5 hp)
Slime A used Acid (2 damage) on Hiro (18/20 hp)
```

From the main script area, make two different characters attack each other.
Try to let the furthest-"down" (in terms of ownership) thing control the behavior.
The main script shouldn't poke at the characters' internal data (abilities or hp).
The characters shouldn't care about the details of what their abilities do.

### Hints

<ol>
<li>Add an <tt>attack(self, target)</tt> function to the Character class.</li>
<li>Add a <tt>perform(self, source, target)</tt> function to the Ability class.</li>
{% include spoiler-hint.html major=2 minor=1
    summary="My<tt>self</tt> is not your<tt>self</tt>"
    details="Note how <tt>self</tt> really isn't <em>that</em> special.  It's a function parameter like any other.  If you pass <tt>self</tt> along to another function, the object being sent along can be called by another name in that next function.
" %}
</ol>

[The completed example.]({{ site.baseurl }}{% link /assets/rpg-2.py %})

---

## Calling partent/superclass functions

```python
class Dog(object):
    def __init__(self, fur_color):
        self.fur_color = fur_color

class BigRedDog(Dog):
    def __init__(self):
        Dog.__init__(self, 'red')
```

Recall class functions are just like normal functions in a different scope, plus the <tt>self</tt> syntactic sugar.
You can call functions from your parent class (or, really, any class) if you need to make use of them.

> If you're coming from other languages, you may see the problem with directly saying `Dog.__init__()`.
> What happens if BigRedDog is changed to inherit from Cat or <tt>object</tt> instead?
> In other languages, this would be an issue.
> In Python, it's still just a function, and data is still named (rather than addressed).

There is a fancier way to call a superclass function to prevent the possible future headache if your superclass changes.
It's recommended that you do this fancier thing, but don't fret too much if this looks weird.
It's using a somewhat advanced Python feature.
This is one area where things are a little more awkward with Python than with some other languages.

```python
class Dog(object):
    def __init__(self, fur_color):
        self.fur_color = fur_color

class BigRedDog(Dog):
    def __init__(self):
        super(BigRedDog, self).__init__('red')
```

You can read more about `super()` [here](https://docs.python.org/2.7/library/functions.html#super).
Why don't you have to pass "self" to the `__init__` call?
Because `super()` is a weird "proxy object"; read more in that link if desired.
Just think of `super()` as returning <tt>self</tt>, but looking at <tt>self</tt> as if it were its superclass' type instead.
Then that `__init__()` call you see is just using the previously mentioned syntactic sugar to not have to pass anything extra to it to make its <tt>self</tt> work.

If you're using Python 3, `super()` is a bit easier to use:

```python
class BigRedDog(Dog):
    def __init__(self):
        super().__init__('red')
```

---

## Exercise: Adding different ability behaviors

```python
chris@CSU:~/work/ZeroToBoto$ python assets/rpg-3.py 
Hiro (20/20 hp)
Slime A (5/5 hp)
Slime B (5/5 hp)
 
Slime A used Acid (2 damage) on Hiro (18/20 hp)
Slime A used Acid (3 damage) on Hiro (15/20 hp)
Slime B used Acid (2 damage) on Hiro (13/20 hp)
Slime C used Disintegrate (9 damage) on Hiro (4/20 hp)
Slime C used Disintegrate (9 damage) on Slime C (0/5 hp)
Hiro used Heal (8 healing) on Hiro (12/20 hp)
```

Create three new kinds of abilities.
1. Healing.
    - Increase HP by an amount, capped at the target character's maximum HP.
    - When used, this ability should print out a different message to indicate that it's healing (not damaging).
2. Ability will increase the amount of damage it deals each time it's used.
    - Be mindful that your damage growth is stored per-object/-instance.  Not per class.
    - Give two characters this ability.  Have one use it twice, *then* the other use it once.  Make sure the first character's use doesn't increase the second's damage dealt.
3. Ability attacks twice.
    - The example attacks the given target, then attacks itself.  You can change this up a little if you want.  But make sure it attacks twice.

In all cases, and in programming in general, try not to repeat yourself.
The point of things is to have the computer handle repetitive tasks, not a human.
You ideally want to have only one place where HP is adjusted by ability damage.
Have one place where that one ability's damage grows.
And so on.

### Hints

1. Healing is the negation of damage.
2. Remember to use <tt>self</tt> accordingly.
3. Calling on help from superclasses can be very handy.


[The completed example.]({{ site.baseurl }}{% link /assets/rpg-3.py %})

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
Items are easy to access at random by *indexing* the dictionary with an item's key.
However, dictionaries don't have a specific human-ey order to them.
So if you're enumerating items in a dictionary without using their keys, rely on not getting them in a predictable order.

Dictionaries use curly braces `{}`, as opposed to lists' square brackets `[]`.
You can create them empty (like "stats" above), or with some items already in them (like "turtles" above).
If defining key-value pairs when you declare the dictionary, the format is `key: value,key2: value2`, and so on.
To add key-value pairs into a dictionary (officially the `dict` type) later on, index the dictionary with the desired key, and assign to it the desired value.

[<tt>dict</tt> documentation.](https://docs.python.org/2.7/library/stdtypes.html?highlight=dict#dict)

---

## Exercise: Making it interactive

```bash
chris@CSU:~/work/ZeroToBoto$ python assets/rpg-complete.py 
Your abilities:
  Slash (4 damage)
  Heal (8 healing)
Remaining combatants:
  Hiro (20/20 hp)
  Slime A (5/5 hp)
  Slime B (5/5 hp)
<ability> <combatant>: slash slimea
Hiro used Slash (4 damage) on Slime A (1/5 hp)
Slime B used Acid (2 damage) on Hiro (18/20 hp)
Slime A used Acid (2 damage) on Hiro (16/20 hp)
 
Your abilities:
  Slash (4 damage)
  Heal (8 healing)
Remaining combatants:
  Hiro (16/20 hp)
  Slime A (1/5 hp)
  Slime B (5/5 hp)
<ability> <combatant>: slash slimea
Hiro used Slash (4 damage) on Slime A (0/5 hp)
Slime B used Acid (3 damage) on Hiro (13/20 hp)
Slime A has died!
 
Your abilities:
  Slash (4 damage)
  Heal (8 healing)
Remaining combatants:
  Hiro (13/20 hp)
  Slime B (5/5 hp)
<ability> <combatant>: heal hiro
Hiro used Heal (8 healing) on Hiro (20/20 hp)
Slime B used Disintegrate (9 damage) on Hiro (11/20 hp)
Slime B used Disintegrate (9 damage) on Slime B (0/5 hp)
Slime B has died!
 
Cleared!
```

Use what you learned from the guessing game and hangman to make a turn-based combat encounter.
The user should input an ability name, and a target to use it on.
Notice from the example usage above I'm calling targets "slimea", "hiro", etc.
You can do hand-set keys like that, or do some smart conversion of their name (`.lower().strip()`, and so on) to make things more dynamic.
That is, easier to change, because you repeat yourself less often.

In addition to making it interactive, you'll notice characters now have multiple abilities at their disposal.

The combat should end only when the player is the only one left standing, *or* the player's HP is at or below 0.
For the enemies, just make them pick a random attack from the set they have available, and always target the player.

### Hints

1. The random module has a function called `choose()` you should look up.
2. Watch out for keys that aren't actually in dictionaries.  Things are case-sensitive!
3. This is a somewhat significant step up from the previous exercise, and from hangman.  Don't expect it to be immediately obvious.
	Keep at it, and maybe try breaking out pieces you can test on their own before coming back to add them to your combat encounter program.

[The complete RPG combat.]({{ site.baseurl }}{% link /assets/rpg-complete.py %})

---

## Extra credit

1. Be more informative/helpful when the player doesn't know the key names for monsters.
2. Give attacks a chance to miss (accuracy rating).  Print it out when listing attacks.  Or, give them a chance to critically hit for double damage.
3. Make up a new attack type, and implement it.  You may have to change the Attack class and/or the combat code.  Suggestions:
    - Attack all targets in a list.
    - Make an attack have a certain number of charges available (think items or mana).

