Title: Intro to Python
sortorder: 333

<div class="embed"><iframe src="https://www.youtube-nocookie.com/embed/Ae4Ow5DvYtE" frameborder="0" allowfullscreen></iframe></div>

## Notes

There are two versions of Python, Python 2 and Python 3. For this guide we will be using Python 3, which you will need to install on your computer. The easiest way to do this, on a Mac, is with Homebrew, a tool that allows you to install and manage command line programs.

### Install Homebrew

Visit [Homebrew's website](https://brew.sh/) and follow the instructions there, or just copy and paste the following into your terminal:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
```

### Install Python 3

Once Homebrew is done, you can use it to install Python and a number of other extremely useful command line tools.

```bash
brew install python3
```

---

### Install a Text Editor

To create and edit Python files you'll need a good text editor, specifically designed to edit code. Here are a few good options:

* [Visual Studio Code](https://code.visualstudio.com/)
* [Atom](https://atom.io/)
* [Sublime](https://www.sublimetext.com/) (not free)


---

## Basics

Python is a command line application, just like `cat`, `grep` and `sort`.

To execute Python code you run the `python` command with a text file as an argument.

To start, let's make a simple program that prints a message on the terminal. To do this we will use the `print` command.

Create a new file called `hello.py` and put this in it:

```python
print("Hello comrade")
```

Open your terminal and navigate to the directory where the file is saved, and then type:

```python
python hello.py
```
You should see "Hello comrade" printed on the screen.


### Expressions

An "expression" is a set of instructions for the computer to execute. Python will read or evaluate your expressions and return a result. For example you can add numbers:

```python
print(1+1)
print(10/2)
print(100 * 6.2 - 70/3.5)
```

You can also test to see how different expressions relate to each other. 

`==` tests for equality  
`<` less than  
`>` greater than  
`<=` less than or equal  
`>=` greater than or equal  

```python
print(1 == 1)
print(1 == 2)
print(1 < 2)
print(5 * 20 >= 100/13)
```
All of these expressions will evaluate to either a `True` or a `False`

---


### Variables

You can store the value of expressions inside named variables using the `=` symbol.

```python
x = 2
y = 5
z = x + y
print(x * 100)
print(z)
```

#### Types

Values have different "types" or categories. For example, 1 is an integer, 1.5 is a float.

You can see what type a value is is by using the `type` function:

```python
print(type(1))
```

Some important types are:

```python
a_number = 1 				# an integer
another_number = 5.1 		# a float
some_string = "Hello!" 		# a string
some_boolean = True 		# a boolean (notice the capitalization)
a_list = ["a bunch", "of", "stuff", a_number, some_string]
a_dictionary = {"key1": 10, "key2": "a string"} # a dictionary (key/value pairs)
```

In Python you do not need to declare variable types, or even that you are declaring a variable, you simply type a name, the equals sign, and then a value or expression.

---


### Strings

Strings are a variable type that stores text. To create a string, surround some text within quotation marks. It doesn't matter if you use single or double quotes as long as you are consistent.

```python
first_name = "Karl"
last_name = 'Marx'

print(first_name)
print(last_name)
```

If you add two or more strings together, Python will combine a new string for you.

```python
first_name = "Karl"
last_name = 'Marx'

print(first_name + last_name)

print(first_name + " " + last_name)
```

Each character in a string is indexed numerically, and can access individual characters using `[]` square brackets. 

```python
name = "Karl Marx"
first_letter = name[0]
print(first_letter)

second_letter = name[1]
print(second_letter)
```

The character index begins with the number 0. If you wish to access the last character, you use `-1`. The second to last, `-2` and so on.

```python
name = "Karl Marx"
last_letter = name[-1]
print(last_letter)
```

You can also get a range of characters in a string by entering a starting and ending index in your square brackets:


```python
name = "Karl Marx"
first_three_letters = name[0:3]
print(first_three_letters)
```

To get the total length of a string, use the `len()` function.

```python
print(len("hello!"))
```

You can also determine if a string exists within another string with the `in` keyword.

```python
sentence = "A spectre is haunting Europe"
print("spectre" in sentence)
```


#### String methods

Python's string implementation comes with many useful methods that allow you to transform and get information about strings.

For example, to make a string uppercase:

```python
sentence = "hello there!"
uppercase = sentence.upper()
print(uppercase)
```

Here are a few more examples of things that you can do

```python
sentence = "   HELLO THERE   "

# make it uppercase
lowercase_sentence = sentence.lower()

# make it title case
titlecase_sentence = sentence.title()

# remove white space at the start and end
stripped = sentence.strip()

# replace one set of characters with another
goodby_sentence = sentence.replace("HELLO", "GOODBYE")
```

Here's a full list: [https://docs.python.org/3.7/library/stdtypes.html#string-methods](https://docs.python.org/3.7/library/stdtypes.html#string-methods)

---


### Lists

A list is a numerically ordered collection of values, also known as an array.

```python
# make an empty list
my_list = []

# add something to our list with the "append" method
my_list.append("hi") # the list will now look like this: ["hi"]

# add some more stuff
my_list.append(45)
my_list.append(100.2)
my_list.append("whatever")

# now our list will look like this:
# ["hi", 45, 100.2, "whatever"]

# get the length of a list
len(my_list)

# you can access individual items in the list by referrring to their index value
print my_list[0] # prints "hi"
print my_list[2] # prints 100.2

# use negative numbers to start at the back
print my_list[-1] # prints "6" - the last item

# you can access part of a list with a ":"
my_list[1:3] # will be [45, 100.2, "whatever"]
```

You can iterate through every value in a list with the `for` keyword:

```python
for item in my_list:
	print(item)
```

---


### Dictionaries

TK

---

### Methods

TK

---


### Reading files

To open a file in Python, use the `open()` keyword function. The function takes two arguments. The first is the name of the file to open, and the second is a flag that states if we are opening the file with the intent of *reading* to it (use "r"), or *writing* to it (use "w").

Once we have opened a file, we use the `read` function to grab it's contents and return then as a string.

In this example, we open a file and store its contents in a string. We then uppercase the entire file and print it to the screen.

```python
content = open("communist_manifesto.txt", "r").read()
loud_manifesto = content.upper()
print(loud_manifesto)
```

You can also store a file as a list of lines using `readlines()` instead of `read()`

This example prints the first 5 characters of a text file.

```python
all_lines = open("communist_manifesto.txt", "r").readlines()
for line in all_lines:
	print(line[0:5])
```


