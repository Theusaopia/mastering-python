name = 'Matheusin o desgraçadão'
age = 23 + 1
height = 170 # cm
height_inches = round(height * 0.393700787)
weight = 62 # up until now kilograms
weight_pound = round(weight * 2.20462)
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} centimeters tall.")
print(f"He's {weight} kilograms heavy.")
print("That's not heavy at all.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the coffee.")

print(f"Height in inches: {height_inches} and Weight in pounds: {weight_pound}")

total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}")
