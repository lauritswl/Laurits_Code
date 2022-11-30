The object oriented paradigm focuses on:
- breaking the code into minor objects that becomes the whole program when combined.
	- those smaller objects become modules that can be reused and broken into smaller models.
How to use object oriented programming:
When modelling an object you model have to define its attributes and methods.
i.e. what it has and what it does:
e.g. when modelling a *waiter*
**Attributes (has):**
``` python
is_holding_plate = True
tabler_responsible = [4,5,6]
```

**Methods (does):** 
``` python
def take_order(table,order):
	#takes order to chef


def take_payment(amount):
	#add money to resturant
```
Methods are defined as functions, but inside of a class.
``` python
class Car:
	def __init__(self) #Attributes set at initializing
		self.seats = 5
	def enter_race_mode(self): #Method for turning car into racecar.
		self.seats = 2
```


## Objects
When we find the attributes and methods of an object we can create multiple versions of that blueprint. The **blueprint** that creates **objects** are called *class*.
``` python
Object = Class()
Waiter_henry = waiter()
```

![[Constructor]]

## [Class Inheritance](https://www.w3schools.com/python/python_inheritance.asp)
**Inheritance** allows us to **define a class** that *inherits* all the *methods and properties* from **another class.**

**Parent class** is the class being inherited from, also called base class.

**Child class** is the class that inherits from another class, also called derived class.
``` python
class Animal:
	def __init__(self):
		self.num_eyes = 2
		
	def breathe(self):
		print("Inhale, exhale.")

class Fish(Animal)
	def __init__(self):
		super().__init__()
		
	def breathe(self):
		super().breathe()
		print("doing this underwater")
		
	def swim(self):
		print("moving in water")

nemo = Fish()
nemo.breathe()
nemo.swim()
######
	#> Inhale, exhale. 
	#> doing this underwater.
	#> moving in water
```
