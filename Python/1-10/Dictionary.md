Dictionaries in python work similarilly to dictionaries in real life.
If you look up a key in the dictionary, you will get the value returned.


### Key vs Value:
**The key** is the equivalent of the *word in the dictionary*
**The value** is the equivalent of the *definition in the dictionary*
### Python syntax:
``` python
dictionary = {
"key" : "value",
"other key" : "another value that defines the key",
"key 3" : "one can continue to add other keys seperated by commas"
}
```
**Retreiving items from a dictionary:**
``` python
print(dictionary("other key")) 
#Prints: another value that defines the key
```
Creating an empty dictionary:
``` python
empty_dictionary = {}
```
Adding new items to an dictionary:
``` python
#Adding new items to an dictionary:
dictionary["key_word"] = "Value assigned to the key"
#Edit an item in a dictionary:
dictionary["key"] = "this key has a new value now"
```
Wiping an empty dictionary:
``` python
dictionary = {}
```
Looping trough a dictionary:
``` python
for key in dictionary:
    print(key) #print all key names
    print(dictionary[key]) #print all values
```
## Nesting:
You can also nest lists or dictionaries inside a dictionary:
``` python
nested_dict{
	key : {dict}
	key2 : [list],
}
```
*or alternatively*;
``` python
#Nest dictionary in a list:
travel_log [{
  "Country":"France",
  "Cities":["Paris", "Lille", "Dijon"], 
  "Times": 12
  },
 {"Country":"Germany",
 "Cities":["Berlin", "Hamburg"], 
 "Times": 5
 }]

```