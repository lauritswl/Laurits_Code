Funtions with inputs will require an input to run, the function the uses this input in its functionality:

## Normal function
``` python
def greet():
    print("Hello Marcus")
    print("Are you doing well?")
    print("Im doing well...")
```
## Function with input
``` python
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Are you doing {name}?")
    print("Im doing well...")
```
or in programming lingo:
``` python
def my_function(parameter)
	print(f"this is the {parameter}")
my_function(argument) # prints: this is the argument
```

## Function with two parameters:
``` python
def greet_with(name,location):
    print(f"hello {name}, what is it like in {location}")
```

# Arguments
## Positional arguements:
``` python
def my_function(a,b,c):
    do_this_with(a)
    then_print(b)
    and_update(c)
```
when calling the function, you can use positional arguements:
``` python
my_function(1,2,3)
    do_this_with(1)
    then_print(2)
    and_update(3)
```
or you can alternatively use keyword arguemetns to call the function:
## Keyword arguments:
``` python
my_fynction(c = 1, a = 3, b = 2)
	do_this_with(3)
    then_print(2)
    and_update(1)



```