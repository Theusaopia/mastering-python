# from system import the argv library
from sys import argv

# setting the cmd arguments as variables
script, filename = argv

# opening the file and setting as a variable
txt = open(filename)

# printing the file name
print(f"Here's your file: {filename}")

# reading the text through the read() method
print(txt.read())

# closing my IO
txt.close()

# asking the user to input the file name again
print("Type the filename again:")
file_again = input("> ")

# opening the file and setting as a variable
txt_again = open(file_again)

# printing the text again
print(txt_again.read())

# closing my IO
txt_again.close()
