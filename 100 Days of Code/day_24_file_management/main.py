with open("my_file.txt", mode="r") as file:
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="w") as file:
    file.write("New Text.")

with open("my_file.txt", mode="a") as file:
    file.write("\nAppended Text")


