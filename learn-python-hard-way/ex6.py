# creating an integer variable
types_of_people = 10

# creating a formated string
x = f"There are {types_of_people} types of people."

# creating a normal string
binary = "binary"

# creating a normal string
do_not = "don't"

# creating a formated string
y = f"Those who know {binary} and those who {do_not}"

# printing string x
print(x)

# printing string y
print(y)

# printing a formated string
print(f"I said: {x}")

# printing a formated string
print(f"I also said: '{y}'")

# creating a boolean variable
hilarious = False

# creating a string with space for one variable
joke_evaluation = "Isn't  that joke so funny?! {} or {}"

# using the method format to include a variable in the open space of joke_evaluation
print(joke_evaluation.format(hilarious, True))

# creating a normal variable
w = "This is the left side of..."

# creating a normal variable
e = "a string with a right side."

# concatenating variables w and e
print(w + e)
