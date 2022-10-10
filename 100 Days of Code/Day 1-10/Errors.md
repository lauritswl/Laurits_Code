## Syntax Error
Syntax errors happen when your code does not make any sense to the computer. This can happen because you've misspelt something or there's too many brackets or a missing comma..

## Name Error 
This happens when there is a variable with a name that the computer does not recognise. It's usually because you've misspelt the name of a variable you created earlier. Note: variable names are case sensitive!

## Indentation Error
This happens if your code is *indented*, by pressing tab or space before the keywords:
``` python
#correct
print("Hello world!")

#Indentation error
 print("Hello world!")

```

## Type Error
The **TypeError object represents an error** when an operation could not be performed, typically (but not exclusively) *when a value is not of the expected type*.
Can be provoked by using an interger in a len() function:
``` python
len(3456) #Result: Type error
	#If we format the number as a **string** the function will work:
len("3456") #Result: 4
```