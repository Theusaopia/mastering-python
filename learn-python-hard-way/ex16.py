from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target =  open(filename, 'w')

print("Truncating the file. Goodbye!")
# target.truncate() I don't need this because the 'w' already does it

print("Now I'm going to ask you for three lines.")

line1 = input("> ")
line2 = input("> ")
line3 = input("> ")

print("I'm going to write these to the file.")

target.write(f"""
{line1}\n{line2}\n{line3}
""")

target = open(filename)

print("New text. What do you think?")
print(target.read())

print("And finally, we close it.")
target.close()
