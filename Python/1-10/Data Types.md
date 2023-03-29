# Data Types in python:
If you use the wrong data type in python, it will output a [[Errors#Type Error|Type Error]].
## Checking Data types
You can use the type() function to check what is the data type of a particular variable.
``` python
n = 3.14159 
type(n) 
#result float
```
### Converting Data Types
You can convert a variable from 1 data type to another:
``` python
#Converting to float:
float(var) 
#Converting to int:
int(var) 
#Converting to string: 
str(var)
```

## Numbers
### Integers
**Intergers are whole numbers**
``` python
my_number = 345
```
For large intergers you can use underscores to as seperaters instead of commas
``` python
million = 1_000_000
print(million) #Prints: 1000000
type(million) #Output: interger
```
### Floating Point Numbers
**Floats are numbers with decimal places.** 
When you do a calculation that results in a fraction e.g. 4 ÷ 3 the result will always be a floating point number.
``` python
my_float = 3.14159
```
**### CAREFULL! ###**
``` python
print(8/3) #prints: 2.666666
print(int(8/3)) #prints: 2
#So use
print(round(8/3),2 #number after comma decides decimal places)
#prints: 2.67  
```


### Interactions:
``` python
my_interger = 3
my_float = 0.14159
my_interacting_number = my_interger + my_float
print(my_interacting_number) #result: 3.14159
type(my_interacting_number) #result: float
```
### Converting to float:
``` python
n = 354 
new_n = float(n)
print(new_n) #result 354.0
```

## String
A **String** is a *string of characters with a fixed order*, It should be surrounded by double quotes.
A strings characters can be accesed by square bracets, that starts at 0.
``` python
"Hello"[0] # Output: H
"Hello"[4] # Output: o
```
### String Concatenation
You can add strings to string to create a new string. This is called concatenation. 
It results in a new string:
``` python
"Hello" + "Angela" 
#Output: "HelloAngela"
```
### Escaping a String
Because the **double quote is special**, it *denotes a string*, if you want to use it in a string, you need to **escape it with a backslash".** 
``` python
speech = "She said: \"Hi\"" 
print(speech) 
#prints: She said: "Hi"
```
### F-Strings
You can **insert a variable into a string using f-strings**. The syntax is simple, just insert the variable in-between a set of curly braces {}
``` python
days = 365 
print(f"There are {days} days in a year") #Prints: There are 365 days in a year
```

## Boolean
Booleans are either True or False, they don't have quotation marks around them, otherwise it would turn them into a String. 
``` python
true_bool = True
false_bool = False
```
