# Chapter 1: Python Basics
Python itself is a programming language. When you run python, you first will have trouble finding out what is going on. The more programs you write and the more you engage in programming, the easier it will get.
When you run "python", the so-called IDLE (Integrated Development Environment) opens. It should look like shown in the picture.
![Python IDLE](/img/Python_shell_home.png)
There are two different ways to write Python code: By writing single-line commands in the *interpreter* or via running whole scripts.
For very simple programs, it is enough to use the Python interpreter. See the three `>>>`? This is where we will start to write programs.

## Hello, world! or getting started with Python
Traditionally, in programming, the first thing to do when learning a new programming language is `Hello, world!`. In Python, this is very simple (you do not have to copy `>>>`, that is just to indicate that it is written in the Python interpreter). Just type
```python
>>> print("Hello, world!")
```
... and that is it! In order to run your program, hit `Enter`. Already, for this simple program to work, a lot of things are going on. `print()` does a very simple thing. It just tries to display the contents inside the parentheses. More about this in later exercises.

**Try it out!**

Congratulations on your (potentially) first program ever written! If you want to, try changing the text inside the `print` statement. What happens if you do `print(Hello, world!)` i.e. leaving out the quotation marks?

## Variables and statements and types
Now, finally that we have an idea on how to use `print()`, we can advance to nicer programs. A very important aspect of programming are something called **variables**. Just like in Mathematics, we can assign values to things. Try it out, write the following statements, one by one:
```python
>>> x = 5
>>> y = 3
>>> print(x+y)
8
```
As you probably expected, this will print out `8`. No surprise so far.
Interestingly, we can overwrite variables: Type out
```python
>>> x = 5
>>> superBigNumber = 3133723666
>>> x = 7 + x
>>> print(x + superBigNumber)         
3133723678
```
Who said variable names had to be boring?
***
Despite all humour, variable names should be useful. For example if your program is storing your height, you might actually call it `height`. People sometimes use useless names for their variables - do not be like these people. Sooner or later, as programs get more complex (commercial applications often have 100 000s lines of code!) good naming gets important.
***
In this example, multiple things are happening at once. First of all, in Mathematics, something like `x = y + x` does not make much sense: The two statements at each side have different values. However, in Computer Science, things are not necessarily how they are in Mathematics. Actually, when Python tries to understand what you have written, it first tries to find out the value on the *right side of the equation* before assigning the value to the left.

In fact, anything executed in Python are so-called *statements*. Here, every statement gets executed once we hit the `Enter` key.

Despite the difference to Mathematics, there are still things that apply. Try out multiplication:
```python
>>> print(4 * 5)
20
```
This works fine. But what is with division?
```python
>>> print(4 / 5)
0
```
Huh. What happened here? Well. Normal division in Python just slices off what would be after the dot in a division. This is because Python variables have something called *type*. We say a **variable is of a certain type**.

##Python types
We have already seen the type of whole numbers, i.e. 5, 3, 9, 14275855431 or -3014. These numbers are called **integers**. Similarly, Python has numbers with positions after the dot, so-called **floating-point numbers** (computer scientists call them *float*). The good thing about division with floats is that Python is able to do division with positions after the dot. Already, we see that Python tries to understand the statements that we write and interpret them in the most intelligent way it can: If a variable is of type **integer**, division stops before the dot, otherwise,the result is no integer any more! Similarly with floats: Division with floats will always (actually, only in most cases) ending in floats.
```python
>>> print(4.0 / 5)
0.8
>>> print(8.5/0.25)
34.0
```
There is one more thing with types: When trying to use different types together, we get into a whole different world.
One of the other types are so-called **strings**. Strings are defined as a series of characters - sounds too complicated, why not just say a series of letters/words, you say? Well, you see, while we as humans usually have pretty normal sentences like "Buy a house", something like "asdklfnea;sefkanfei383912rn12n52112,5.,125,21.}" is also a valid string, although it may not necessarily be what we as humans see as Strings.

Strings are awesome! Try the following:
```python
>>> myName = "Peter"
>>> myFriendsName = "Paul"
>>> print(myName + " is friends with " + myFriendsName)
```
What happens? Well, the result `Peter is friends with Paul` gets printed. As you can see, we can use the `+` operator for "adding" strings to one another. When Python computes the values in the `print()` statement, it actually first combines the individual elements. We call this procedure of adding things to the end of other things **appending** i.e. `" is friends with " gets appended to myName`.

###todo: lists, dicts? functions on lists? input?


## Conditional statements
## Loops
## Arrays and Whack-A-Mole
