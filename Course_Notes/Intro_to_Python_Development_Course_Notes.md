07/12/2023
rhurst@wabtec.com

# Course Notes

Since I am doing quite a but on my work laptop I wanted to be able to code in the Windows environment. So I did the following: 

	1. Went to https://www.python.org/downloads/ downloaded the 3.11.4 version,e else Visual Studio Code (VSC) will not have access to the libraries to code and run Python funcitons
	2. Already had Visual Studio Code installed but installed Python and Pylance extensions 
	
VSC can now run REPL (Read Execute Print Loop) in the terminal by fir typing in "py" into the termianl once you open the terminal in VSC

In these notes I am skipping his first introductory videos and just noting the meat an potatoes of Python. If you want a more "Linux" friendly version, watch the first 6 or so videos. 
Will allow for linux set up for Paths etc that is specific to linux versus the Wondow environment. 

First I created a simple hello.py file that ran some very basic print and math. I imported timE to evoke the time.sleep function to limit the rate at which everything ran.

## Lesson 4.1 Strings

Instructor references https://docs.python.org/3/ to start as it is the authority on all of the Python language and you should get familiar with it. He references 
the Library Reference -> Built in Types and goes to str for String.

The mostnotable is a string instance by the following syntax per the docs: (note the back ticks `` are for the markdown syntax to use code block)

` 'hello'.capitalize() `

This will return 'Hello' THere are alot of methods for all of the standard types

## lesson 4.2 Numbers

Once again, reference docs @ https://docs.python.org/3.11/library/stdtypes.html#numeric-types-int-float-complex

One notable thing from this lesson is creating a string from a number like:

` str(7.23)` hten defines the number as a string and will return as such and set the string with those characeters. smae goes with float, etc. So if you ingested a tring and wanted 
to cnvert it to a number you could do:
`float('799.23')` 

this would cconvert hte sting characters to a number you you work math or similar on. 

## Lesson 4.4 Lists: 
defined by name then [] with comma seperators. Like my_list = [1,2,3,4,5,6,7]

Talked function "len" which is length. Can pass 'len(my_list)' and it will return the length. so the example above would return 7

Talked about "slicing" where you can specify a range of your list  to return. Can pass 'my_list[1:4]' Returns staring at the 1 position up to and no including the 4th position. 
would return [2,3,4]
Also the step function uses two :: in the input which if you input 'my_list [::3]' Returns [1,4,7]gives you every third place in the list. 

Negative reverses the lsit and gives quite a bit of options. If you pass 'my_list[::-1] will returnthe lsit in reverse order.

Can reassign list values by calling hte position(s) and assigneing it a new value like 'my_lsit[0]=21' will assign position 0 to a new value of 21 instead of 1. 


## Lesson 4.5 Tuples and Ranges:

Another sequence type like list.

### Tuples:

define like 'point = (2.0, 3.0)' One note that he spoke to is that you cannot change hte length of a tuple or change hte values. However you can unpack them. 

### Ranges
define by myrange(1,10)
is you list the my range it will show you all of the actual numbers in the range.
myrange =range(1,10)
if you command 'list(myrange) it will return [1, 2, 3, 4, 5, 6, 7, 8, 9]

## Lesson 4.6 Dictionaries

Is a Colection Type have named indexes, example: 

 ages = { 'kevin' :29, 'alex': '30', 'ryan': 49}
 
 this is liske a list where the numeric values after the colons are the value buth te names are the index. A list or tuple would have hte value of 
 29 assigned to the 0 index and hte value of 30 at the 1 index and the value of 49 at the 2 index. Instead we are in essence have the abilit to define the index
 by placing the "" and name for it. 
 print(mydict['alex'])
 
 can change each one or delete instances similar to lists
 
 can call 'dict' function
 
# Chapter 5 Control Flow
 
## Lesson 5.1 Conditionals and Comparisons

### Comparisons: 

- < less than
- \> Greater than 
- <= less than or equal
- \>= greater than or equal
- == equal 
- != not equal is object identity
- is not negated object identity

basic stuff here showing the comparison operators. 
```
2 in [1, 2, 3]
True
4 in [1, 2, 3]
False
2 not in [1, 2, 3]
False
4 not in [1, 2, 3]
True
```
```
 name = "Kevin"
>>>if len(name) >= 6:
     print("name is long")
... elif len(name) == 5:
...     print("name is 5 characters")
... elif len(name) >= 4:
...     print("name is 4 or more")
... else:
...     print("name is short")
...
name is long
```
## Lesson 5.2 Logic Operations

Boolean Operators (https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not )

Not operation: 
```
>>> name = ""
>>> not name
True
>>> if not name:
...     print("No name given")
...
>>>
```
Or operation: 
```
first = ""
>>> last = "Thompson"
>>> if first or last:
...     print("The user has a first or last name")
...
The user has a first or last name
>>>
```
And operation: 

```
>>> first = 'Ryan'
>>> last = ''
>>>if first and last:
...    print("the user has a full name)
...
>>>
```
## Lesson 5.3 The While Loop

while statement (https://docs.python.org/3/tutorial/introduction.html#first-steps-towards-programming)

Basic While loop:
```
>>> count = 1
>>> while count <= 4:
...     print("looping")
...     count += 1
...
looping
looping
looping
looping
>>>
```
We can use other loops or conditions inside of our loops; we need only remember to indent four more spaces for each context. If in a nested context we want to continue to the next iteration or stop the loop entirely we also have access to the continue and break keywords:

```
>>> count = 0
>>> while count < 10:
...     if count % 2 == 0:
...         count += 1
...         continue
...     print(f"We're counting odd numbers: {count}")
...     count += 1
...
We're counting odd numbers: 1
We're counting odd numbers: 3
We're counting odd numbers: 5
We're counting odd numbers: 7
We're counting odd numbers: 9
>>>
```
In that example, we also show off how to "string interpolation" in Python 3 by prefixing a string literal with an f and then using curly braces to substitute in variables or expressions (in this case the count value).

Here's an example using the break statement:

```
>> count = 1
>>> while count < 10:
...     if count % 2 == 0:
...         break
...     print(f"We're counting odd numbers: {count}")
...     count += 1
...
We're counting odd numbers: 1
```

## Lesson 5.4 The For Loop

It's incredibly common to need to repeat something a set number of times or to iterate over content. Here is where looping and iteration come into play.

Python Documentation For This Video
for statement (https://docs.python.org/3/tutorial/controlflow.html#for-statements)

The TEMP_VAR will be populated with each item as we iterate through the SEQUENCE and it will be available to us in the context of the loop. After the loop finishes one iteration, then the TEMP_VAR will be populated with the next item in the SEQUENCE, and the loop's body will execute again. This process continues until we either hit a break statement or we've iterated over every item in the SEQUENCE. Here's an example looping over a list of colors:
```
>>> colors = ['blue', 'green', 'red', 'purple']
>>> for color in colors:
...     print(color)
...
blue
green
red
purple
```
If we wanted not to print out certain colors we could utilize the continue or break statements again. Let's say we want to skip the string 'blue' and terminate the loop if we see the string 'red':
```
>>> colors = ['blue', 'green', 'red', 'purple']
>>> for color in colors:
...     if color == 'blue':
...         continue
...     elif color == 'red':
...         break
...     print(color)
...
green
>>>
```
Other Iterable Types
Lists will be the most common type that we iterate over using a for loop, but we can also iterate over other sequence types. Of the types we already know, we can iterate over strings, dictionaries, and tuples.

Here's a tuple example:
```
>>> point = (2.1, 3.2, 7.6)
>>> for value in point:
...     print(value)
...
2.1
3.2
7.6
>>>
```
A dictionary example:
```
>>> ages = {'kevin': 59, 'bob': 40, 'kayla': 21}
>>> for key in ages:
...     print(f"{key} is {ages[key]}")
...
kevin is 59
bob is 40
kayla is 21
```
Unpacking Multiple Items in a for Loop
We discussed in the tuples video how you could separate a tuple into multiple variables by "unpacking" the values. Unpacking works in the context of a loop definition, and you'll need to know this to most effectively iterate over dictionaries because you'll usually want the key and the value. Let's iterate of a list of "points" to test this out:
```
>>> list_of_points = [(1, 2), (2, 3), (3, 4)]
>>> for x, y in list_of_points:
...     print(f"x: {x}, y: {y}")
...
x: 1, y: 2
x: 2, y: 3
x: 3, y: 4
```
# Chapter 6 Encapsulating Code

## Lesson 6.1 Writing Functions

Defining Functions (https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

key word is "def" to call out the function
example: 
```
>>> def hello_world():
...    print("hello world!!") 
... 
>>> hello_world()
hello world!!
```
If we want to define an argument, we will put the variable name we want it to have within the parentheses:
```
>>> def print_name(name):
...     print(f"Name is {name}")
...
>>> print_name("Keith")
Name is Keith
```
Let's try to assign the value from print_name to a variable:
```
>>> output = print_name("Keith")
Name is Keith
>>> output
>>>
Neither of these examples has a return value, but we will usually want to have a return value unless the function is our "main" function, or carries out a "side-effect" like printing. If we don't explicitly declare a return value, then the result will be None.
```
You have to use the return keyword to actually return a value. 

We can declare what we're returning from a function using the return keyword:
```
>>> def add_two(num):
...     return num + 2
...
>>> result = add_two(2)
>>> result
4
````
Every function call we've made up to this point has used what are known as positional arguments, but if we know the name of the arguments and not necessarily the positions we can call them all using keyword arguments like so:
```
>>> def contact_card(name, age, model):
...     return f"{name} is {age} and drives a {model}"
... 
>>> contact_card("ryan", 50, "HD2500")
'ryan is 50 and drives a HD2500'
```
you can specify the fields out of order by using positional arguements: 
```
>>> contact_card(model = "Chevy 2500 HD", name = "ryan", age=50) 
'ryan is 50 and drives a Chevy 2500 HD'
```
Defining Default Arguments
Along with being able to use keyword arguments when we're calling a function, we're able to define default values for arguments to make them optional when the information is commonly known and the same. To do this, we use the assignment operator (=) when we're defining the argument:
```
>>> def can_drive(age, driving_age=16):
...     return age >= driving_age
...
>>> can_drive(16)
True
>>> can_drive(16, driving_age=18)
False
Default arguments need to go at the end of the arguments list when defining the function, so that positional arguments can still be used to call the function.
```