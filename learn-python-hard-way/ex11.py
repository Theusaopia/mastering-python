print("How old are you?", end=' ') # the end is not to go to a newline
age = input('--> ')

print("How tall are you?", end=' ')
height = input('--> ')

print("How much do you weight?", end=' ')
weight = input('--> ')

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print("\n------Another form------\n")

print("Who's your favorite band?", end=' ')
band = input()

print("Ja oder nein?", end=' ')
option = input()

print(f"{band} is good? {option}")
