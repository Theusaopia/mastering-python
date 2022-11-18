# declaring integer variable
cars = 100

# declaring floating point variable
space_in_a_car = 4.0

# declaring integer variable
drivers = 30

# declaring integer variable
passengers = 90

# declaring operation variable
cars_not_driven = cars - drivers

# declaring a variable with another variable value
cars_driven = drivers

# declaring operation variable
carpool_capacity = cars_driven * space_in_a_car

# declaring operation variable
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
