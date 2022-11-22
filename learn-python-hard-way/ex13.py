from sys import argv # argv = argument variable

script, first, second, third = argv # from left to right assign the args to the variables

print("The script is called:", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)

something_more = input("Do you want more?")

print(f"Here's more: {something_more}")
