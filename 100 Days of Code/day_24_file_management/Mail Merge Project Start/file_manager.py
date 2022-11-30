class File_Manager:
    def __init__(self):
        self.input_string = "attribute that saves read file"
        self.output_string = "attribute thats written in file"

    def read_txt(self, PATH_STRING):
        """Returns contents of txt file as object.input_string"""
        with open(PATH_STRING ,mode="r") as file:
            contents = file.read()
            self.input_string = contents

    def write_txt(self, PATH_STRING):
        with open(PATH_STRING ,mode="w") as file:
            file.write(self.output_string)
