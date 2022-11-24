from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print(f"The input file is {len(indata)} bytes long")
#
# print(f"Does the output file exists? {exists(to_file)}")

print(f"Copying from {from_file} to {to_file}")

open(to_file, 'w').write(open(from_file).read())
