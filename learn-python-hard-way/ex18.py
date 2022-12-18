# this one is like the scripts with argv
def print_two(*args):
    arg1, arg2 = args # four spaces of indentation
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")


def print_one(arg1):
    print(f"arg1: {arg1}")


def print_none():
    print("Got nothing here buckaroo")


print_two("Math", "Dias")
print_two_again("Math", "Dias")
print_one("Math")
print_none()
