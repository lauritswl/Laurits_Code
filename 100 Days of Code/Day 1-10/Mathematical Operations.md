# Mathematical Operations
## Arithmetic Operators 
You can do mathematical calculations with Python as long as you know the right operators.
``` python
3+2 #Add: 5
4-1 #Subtract: 3 
2*3 #Multiply: 6
6/2 #Divide: 3.0 (always a float) 
5**2 #Exponent 
```
**Python follows PEMDAS**
- Parentheses 
	- `()`
- Exponents (Powers, Roots)
	- `**`
- Multiply &  Divide
	- `* & /`
- Add & Substract
	- `+ & -`
*Multiply & Divide* and *Add & Substract* rank equally (and go left to right).
## The += Operator 
This is a convenient way to modify a variable. 
It takes the *existing value* **in a variable and adds to it**. You can also use any of the other mathematical operators e.g. `-=` or `*-`
``` python
my_number = 4 
my_number += 2 
print(my_number) #prints: 6
```
## The Modulo Operator
Often you'll want to know what is the remainder after a division. 
e.g. *4 ÷ 2 = 2 with no remainder* but *5 ÷ 2 = 2 with 1 remainder* 
The **modulo** does **not give you the result** of the division, **just the remainder**. 
It can be really helpful in certain situations, e.g. figuring out if a number is odd or even.
``` python
5 % 2 #result: 1
```
### Number manipulation

``` python
print(8/3) #prints: 2.666666
print(int(8/3)) #prints: 2
#So use round, that uses syntax round(number_to_round,decimal_places)
print(round(8/3),2)
#prints: 2.67  