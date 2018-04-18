---
category: info
info_order: 2
date: 2018-04-18 05:10 -07:00
title: Functions and the stack
---

What are functions?  Why are they useful?  How do they work?

<!-- more -->

Functions are a way of wrapping up a few lines of code so you only have to type them once, instead of typing the same code out every time you want to do something.
Say you only have the "+" and "-" operators available.
If you wanted to multiply 2 times 3, you could just write 2+2+2.
How about 2 times 23?
2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2+2.
No way we're going to do that again and again.
It'll be easier to understand functions and the stack with a detour into assembly-like instructions, register, etc.
Assembly is a broad term for different low-level, human-readable languages.

Each line of assembly is one "instruction"-- also called an "operation"-- that we're telling the computer to perform.
In our made-up assembly language, each line begins with an instruction's short name all in uppercase letters.
After that is any parameters it takes, separated by commas.
Anything to the right of an octothorpe ("#") is a comment.
The computer completely ignores comments.
These are just for humans to explain to each other (or themselves) what's happening.
While first learning to program, comments will tend be very literal/1-to-1 to what the computer is doing; try not to make that a habit, though.
Once you're more comfortable, comments should describe, in plain human language, the _intent_ of some code.
Another human reader can already see the _effects_ by reading the code itself.
So even though code is written for a computer to execute, it should be written with a human audience in mind.
If you can stick to that, your code will be *much* easier for yourself or others to understand.

Now, pay no mind while I ignore all that advice for a while.
Having literal comments per-line is still useful for your first steps.

| Instruction | Parameters              | Explanation |
|-------------|-------------------------|-------------|
| PRINT       | 1: register or constant | Write either the value stored in the register, or the constant, to a display for humans to read.  Has no effect the computer cares about. |
| LOAD        | 2: destination register, constant or source register | Set the destination register's value to the constant or the value of the source register.
| ADD         | 2: destination register, constant or source register | Set the destination register to its value _plus_ the constant or value of the source register.


```
#--- assembly ---
# 2 * 3 hard-coded in assembly-like instructions
LOAD  A, 2   # assign register A the value 2
ADD   A, 2   # add 2 into A (A is now == 2*2)
ADD   A, 2   # add 2 into A (A is now == 2*3)
PRINT A      # outputs "6"
PRINT 15     # outputs "15" (just to show how PRINT supports both registers and constants)

#--- output ---
6
15
```

Now, what about 2 * 4?

```
#--- assembly ---
# 2 * 4 hard-coded in assembly-like instructions
LOAD  A, 2   # assign register A the value 2
ADD   A, 2   # add 2 into A (A is now == 2*2)
ADD   A, 2   # add 2 into A (A is now == 2*3)
ADD   A, 2   # add 2 into A (A is now == 2*4)
PRINT A      # outputs "8"

#--- output ---
8
```

Clearly, this "works", but this is hardly programming.
Hand-writing each multiplication like this isn't going to let anyone be any lazier, which is really what programming's all about.

Registers are always-available places where you can write whatever you want.
Here, we'll pretend registers A, B, C, and D all exist, and are available for arbitrary use by the programmer.
Some special registers will be explained later.

| Instruction | Parameters              | Explanation |
|-------------|-------------------------|-------------|
| PRINT       | 1: register or constant | Write either the value stored in the register, or the constant, to a display for humans to read. |
| LOAD        | 2: destination register, constant or source register | Set the destination register's value to the constant or the value of the source register.
| ADD         | 2: destination register, constant or source register | Set the destination register to its value _plus_ the constant or value of the source register.

