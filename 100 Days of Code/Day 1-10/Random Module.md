# Randomisation
Randomisation is very important for programs that need to be unpredictable.
Computers are deterministic, they will perform predictable actions in certain order.

## Random int

``` python
#Import it:
import random
#Generate random integer between 1 and 10
random_interger = random.randint(1,10)
```

## Random float
``` python
#random float between 0.0000001... and 0.9999999...
random_float = random.random()
#random number between 0 and 4.99999
random_float *= 5
```