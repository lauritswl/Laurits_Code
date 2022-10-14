# Logical Operators
There are 3 really usefull logical operators:
## And Operator
For a **and** statement to be true, both *statementes part of the and statement* must be true, for the statement to be true.
``` python
# Set an variable we want to check
a = 10
# True:
a > 9 and a < 13

# False:
a > 11 and a < 13
```
## Or Operator
For an **or** operator only one condition needs to be true.

``` python
a = 10
#True:
a == 10 or a == 11

#False:
a == 9 or a == 11
```

## Not Operator
For at **not** operator the condition needs to be true.
It therefore reverses the condition
``` python
a = 10
#True:
not a == 11

#False:
not a == 10
```
