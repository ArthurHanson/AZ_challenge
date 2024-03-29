#!/usr/bin/python3
"""
Challenge 2:
Write a program that converts a hexadecimal (base 16) number to decimal number (base 10).

The program must accept as its first argument a path to an input filename.
Each line in this input file contains a hex number.
The hex number does not have the leading 'Ox' and all alpha characters (a through f) are lowercase.
Do not use any built in features of your selected programming language to directly convert from base 16 to base 10.

Input Sample:
9f
11

Output Sample:
159
17
"""
import sys


def usage():
	print("usage: python3 c2.py input-2.txt")
	sys.exit(1)


def hex_to_dec(line: str) -> int:
	"""Return base 10 number given a base 16 number formatted as a string."""
	hex_chars = "0123456789abcdef"
	val = 0
	str_ = line.lower()  # double-check lowercase...
	if not all([var in hex_chars for var in str_]):  # make sure it's valid base 16
		pass
	for i, char in enumerate(reversed(str_)):
		val += hex_chars.find(char) * 16 ** i
	return val


if __name__ == "__main__":
	if len(sys.argv) != 2:
		usage()

	file = sys.argv[1]
	try:
		with open(file, 'r') as f:
			lines = f.readlines()
	except IOError:
		print("Could not read file:", file)
		sys.exit(1)

	lines = [line.strip() for line in lines]
	for line in lines:
		print(hex_to_dec(line))
