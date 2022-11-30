#TODO: Create a letter using starting_letter.txt
from file_manager import File_Manager
file_manager = File_Manager()


# Convert invited.names.txt to list
file_manager.read_txt("./Input/Names/invited_names.txt")
names = file_manager.input_string.splitlines()

for NAME in names:
    file_manager.read_txt("./Input/Letters/starting_letter.txt")  # Read placeholder letter
    file_manager.output_string = file_manager.input_string.replace("[name]", NAME)  # Replace placeholder name with loop object NAME
    file_name = f"letter_for_{NAME}.txt"  # create new lettername
    file_manager.write_txt(f"./Output/ReadyToSend/{file_name}")







#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp