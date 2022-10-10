# print()
## String manipulation and code intelligence:
When printing multiple lines, we can manipulate the string to avoid typing print() multiple times:
``` python
print("Hello world!\nHow are you doing?")
# "Hello world!
#  How are you doing?"
```
print("Hello world!\nHow are you doing?")`

## String Concatenation
Taking seperate string of charectars and merging them into one:

``` python
print("Hello " + "Laurits")
# -> Hello Laurits
```
# input()
The input function allows the user to write a string for the program to use.
The input functions works alot like the print function, you insert a promt that is displayed for the user. The user gets to write a string, that can be saved in a variable or be nested in another function:

``` python
input("What is your name? \n")
```

**Output**: -->
What is your name?
*insert text here*

# Nesting functions:
Nesting a function means that you *write a function, inside of another function:*
``` python
print("Hello " + input("What is your name? \n"))
```
# len()
Output the length of charecters in a string, e.g.:
``` python
len(Laurits) 
#-> 7
```
# Nesting functions:
Nesting a function means that you *write a function, inside of another function:*

``` python
# "What is your name?" -> "Hello *name*"
print("Hello " + input("What is your name? \n"))

# "What is your name" -> *length of name*
print( len( input("What is your name?") ) )
```

## Variables
Assign a string to a variable:
``` python
name = input("What is your name?\n")
# What is your name?
#*write name here*
print(name)
#*name*
```
