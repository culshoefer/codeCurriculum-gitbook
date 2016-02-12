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
What happens? Well, the result `Peter is friends with Paul` gets printed. As you can see, we can use the `+` operator for "adding" strings to one another. When Python computes the values in the `print()` statement, it actually first combines the individual elements.

We call this procedure of adding things to the end of other things **appending** i.e. " is friends with " gets appended to `myName` (If you want to get specifically into the details of programming languages, in the specific case of strings, the process of appending is called *concatenation*, but don't worry about that for now, it is not important).

However, when we try to do the following:
```python
>>> myName = "Peter"
>>> myAge = 876
>>> print(myName + " is " + myAge + " years old")
```
we get an error! That is due to the fact that the `+` does not know what to do in this case: Should it treat the value stored in " is " as a number and literally add it to the integer myAge, or should it treat myAge as a String and append it to " is "? In this case, we have to *tell the operator what to do*. When we want to use numbers (integers, floats) as strings, we put backticks (\`\`) around numbers to convert them to Strings. This procedure of taking a value of one type and chaning it to another type is called `type conversion`. The correct way to do the example above would be:
```python
>>> myName = "Peter"
>>> myAge = 876
>>> print(myName + " is " + `myAge` + " years old")
```
Try it out for yourself!

One more thing: In Python (and also in may other programming languages), there is another data type for individual characters, simply called **characters** (or **chars**). There is a special syntax for chars: Because they are so similar to Strings, we also show them with quotes, but because of their difference, we use single quotes.
```python
>>> someChar = ':'
>>> someOtherChar= 'D'
>>> print(someChar + someOtherChar)
:D
```

The good thing is, because chars are so similar to strings, there is not much

To summarize:

The `print()` function prints results on screen.
Variables have a *type* such as integer, float or String (in fact, there are many more - even only for numbers), a *name* and hold a *value*.


##Simple Python Scripts and input
So far, we have used the python interpreter to print things on-screen. However, if we want to create more complex programs (games!!!) then we have to turn to scripts. To create a new Python script, simply click on `File -> New Window`. A new empty window should open. In this window, you can type commands just like you would in the interpreter. When Python goes through your commands, it does so by starting at the top and working its way through each statement until it reaches the end of the file. So, to familiarize yourself with the new environment, just try out what we did before.

Make a program that displays the following, storing the values of 5 and 58337 internally and then storing the sum, the product and the division in a different variable. After that, print the result to the screen using the newly-learned technique of appending strings:

`The sum of 5 and 58337 is 58342, their product is 291685, and 58337/2 is 29168.5 `

There are many more data types in Python. One very widely used data type are lists.
Lists are nothing more than a collection of items, to which you can add elements, remove some or access particular elements. In Python (in fact in many programming languages), lists are simply created by the following command:
```python
crocodile = 'b'
things = [5, 1.7, crocodile, ]
```


## Conditional statements
## Loops
## Arrays and Whack-A-Mole
