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

Classes are very useful for having a collection of stuff that agrees to some kind of way of interacting with it, and writing very simple code that uses that means of interacting, without necessarily knowing what it's using.
Sounds weird, but it will make sense over time.
Some basic code can operate on a list of *things*, and let them drive what that actually means.
This lets you easily extend some functionality you have later on by just creating one new class and stick an instance of it in a list.
*Without* needing to touch the code you've already debugged and figured out is just right for the basic intent of the program.

```python
class Dog(object):
    def speak(self):
        print 'woof'

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
>>> fido
<__main__.Dog object at 0x7fca85abc310>
>>> type(fido)
<class '__main__.Dog'>
>>> Dog
<class __main__.Dog>
>>> type(Dog)
<type 'type'>
>>> type(fido) == Dog
True
```

When you want to use a class, you create a new <strong><em><u>instance</u></em></strong> of that class (a new *object* of that class' type) by giving the class name followed by parentheses.
It's like there's a function that is the class' name, which gives you back a new one of that class.

Above, notice all functions within a class take the parameter `self`.
`self` is always the instance of the object whose function is being called.
We didn't use `self` in this example-- the function just prints a message no matter which instance it's called on-- but we will in the future.
Naming this first paremeter "self" is just a convention-- you can call it whatever you want-- but please call it "self" for the sake of consistency with basically *all* other Python code out there.

> If you're coming from other languages where this example requires a common base class <tt>Animal</tt> between these two types, this is a bit different in Python.
> Python is strongly typed (Dog is not Cat), but you can also mix and match types about as much as you want.
> So long as a type quacks like a duck and walks like a duck, to Python, it may as well be.
> ... Unless you specifically ask something like `isinstance(fido, Duck())`.


Classes are a convenient way to bundle behaviors and data together.
- You (can) describe the way some *type of thing* works by defining a class and giving it functions.
- You (can) also describe what data personalizes and lives with an *instance* of that class, and manipulate it over time.

For example, you could have a RemoteMachine class with functions like connect(), ping(), disconnect(), restart(), etc.
An individual instance of that class would hold its own IP address, maybe credentials, connected/disconnected state, etc.
That way, you could have multiple machines you're talking to at once, that can all easily repeat the same behavior, but instance of the RemoteMachine class knows what IP to send its pings to.

```python
class RemoteMachine:
    def __init__(self, ip):
        self.ip = ip

    def ping(self):
        response_ms = some_imaginary_module.send_ping(self.ip)
        print response_ms
```

```bash
>>> machines = []
>>> machines.append(RemoteMachine('127.0.0.1'))
>>> machines.append(RemoteMachine('10.0.0.1'))
>>> for machine in machines:
...        machine.ping()
...
0.09
12.2
```

Above, the `ping()` function is a part of the `RemoteMachine` class.
You

---

[The complete RPG combat.]({{ site.baseurl }}{% link /assets/rpg-complete.py %})

---

## Extra credit

1. Be more informative/helpful when the player doesn't know the key names for monsters.
2. Give attacks a chance to miss (accuracy rating).  Print it out when listing attacks.  Or, give them a chance to critically hit for double damage.
3. Make up a new attack type, and implement it.  You may have to change the Attack class and/or the combat code.  Suggestions:
    - Attack all targets in a list.
    - Make an attack have a certain number of charges available (think items or mana).

