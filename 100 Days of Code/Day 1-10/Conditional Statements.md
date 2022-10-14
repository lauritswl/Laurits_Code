# Conditional Statements
Conditional statements are statements that **does something** based on the *conditions state.*

## if-else statement
If-else statements *excecute if:* statement if **condition == variable**.
The *else statement is excecuted* if **condition != variable**
``` python
if statement:
	function_1
else:
	function_2
```

![[If_else.png]]


### Nested if-else statement
A **nested if-else statement** is a statement *nested into* (inside of another) statement
``` python
if condition = variable:
	if another_condition = variable:
		function_1 
	else:
		function_2
else:
	function_3
```
![[Nested if_else.png]]
**or:**
``` python
if condition = variable:
funtion_4
	if another_condition = variable:
		function_1 
	else:
		function_2
else:
	function_3
```
![[nested if_else2.png]]

 ### if / elif / else
checks **if statement first**, then **elif statements** and if none of those are true, it excecutes the **else statement**:
``` python
if condition_1:
	do A
elif condition_2:
	do B
else:
	do C

```
![[elif_flow.png]]

### Multiple If Statements in Succession
Checks if statements indepentently:
``` python
if condition1:
	do A
if condtion2:
	do B
if condition3:
	do C
```
![[Multiple if statements.png]]



## For multiple conditions check [[Logical Operators]]