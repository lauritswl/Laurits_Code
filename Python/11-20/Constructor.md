A **constructor** is part of the *class* that allows us to *specify* what happens when our *object* is being **initialized** (*created*). 
``` python
class User:  
    def __init__(self, id):  
        #initialise attributes  
        print("Print this when new user is created")  
        self.id = id  
  
  
user_1 = User("001")  
print(f"This user_1 has id: {user_1.id}")


### OUTPUT ###
#> print this when new user is created
#> This user_1 has id: 001
```
