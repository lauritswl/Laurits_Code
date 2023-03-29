# Interacting with files 
## (save data outside script)

Opening and **reading** a file:
``` python {read a file}
with open("my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents) 
```

Opening and **overwriting** a file (deleting old text, and writing new text):
``` python {write in a file}
with open("my_file.txt", mode="w") as file:
    file.write("New Text.")
```

Opening and **appending** text file:
``` python {write in a file}
with open("my_file.txt", mode="a") as file:
    file.write("New Text.")
```




